#!/usr/bin/python
# -*- coding: utf-8 -*-
from time import time
import numpy as np
import torch
from torch import nn
import os
from torchvision import transforms  # 추가: transforms 모듈 import
from PIL import Image  # 추가: 이미지를 불러오기 위한 모듈 import

# 현재 스크립트 파일의 절대 경로를 가져옵니다.
script_path = os.path.abspath(__file__)

# 스크립트 파일이 있는 디렉토리 경로를 가져옵니다.
script_dir = os.path.dirname(script_path)

# 작업 디렉토리를 스크립트 파일이 있는 디렉토리로 변경합니다.
os.chdir(script_dir)

# Define the models
def get_pdn(out=384):
    return nn.Sequential(
        nn.Conv2d(3, 128, 4), nn.ReLU(inplace=True),
        nn.AvgPool2d(2, 2),
        nn.Conv2d(128, 256, 4), nn.ReLU(inplace=True),
        nn.AvgPool2d(2, 2),
        nn.Conv2d(256, 256, 3), nn.ReLU(inplace=True),
        nn.Conv2d(256, out, 4)
    )

def get_ae():
    return nn.Sequential(
        # encoder
        nn.Conv2d(3, 32, 4, 2, 1), nn.ReLU(inplace=True),
        nn.Conv2d(32, 32, 4, 2, 1), nn.ReLU(inplace=True),
        nn.Conv2d(32, 64, 4, 2, 1), nn.ReLU(inplace=True),
        nn.Conv2d(64, 64, 4, 2, 1), nn.ReLU(inplace=True),
        nn.Conv2d(64, 64, 4, 2, 1), nn.ReLU(inplace=True),
        nn.Conv2d(64, 64, 8),
        # decoder
        nn.Upsample(3, mode='bilinear'),
        nn.Conv2d(64, 64, 4, 1, 2), nn.ReLU(inplace=True),
        nn.Dropout(p=0.2, inplace=False),  # Dropout 추가
        nn.Upsample(8, mode='bilinear'),
        nn.Conv2d(64, 64, 4, 1, 2), nn.ReLU(inplace=True),
        nn.Dropout(p=0.2, inplace=False),  # Dropout 추가
        nn.Upsample(15, mode='bilinear'),
        nn.Conv2d(64, 64, 4, 1, 2), nn.ReLU(inplace=True),
        nn.Dropout(p=0.2, inplace=False),  # Dropout 추가
        nn.Upsample(32, mode='bilinear'),
        nn.Conv2d(64, 64, 4, 1, 2), nn.ReLU(inplace=True),
        nn.Dropout(p=0.2, inplace=False),  # Dropout 추가
        nn.Upsample(63, mode='bilinear'),
        nn.Conv2d(64, 64, 4, 1, 2), nn.ReLU(inplace=True),
        nn.Dropout(p=0.2, inplace=False),  # Dropout 추가
        nn.Upsample(127, mode='bilinear'),
        nn.Conv2d(64, 64, 4, 1, 2), nn.ReLU(inplace=True),
        nn.Dropout(p=0.2, inplace=False),  # Dropout 추가
        nn.Upsample(56, mode='bilinear'),
        nn.Conv2d(64, 64, 3, 1, 1), nn.ReLU(inplace=True),
        nn.Conv2d(64, 384, 3, 1, 1)
    )

# Check if GPU is available
gpu = torch.cuda.is_available()

# Initialize the models
autoencoder = get_ae()
teacher = get_pdn(384)
student = get_pdn(768)

# Load trained model weights
auto_dir = 'EfficientAD-main/output/8_64jpg/trainings/mvtec_ad/erazer'
teach_dir = 'EfficientAD-main/output/8_64jpg/trainings/mvtec_ad/erazer'
stu_dir = 'EfficientAD-main/output/8_64jpg/trainings/mvtec_ad/erazer'
autoencoder_load = torch.load(os.path.join(auto_dir, 'autoencoder_final.pth'))
teacher_load = torch.load(os.path.join(teach_dir, 'teacher_final.pth'))
student_load = torch.load(os.path.join(stu_dir, 'student_final.pth'))

# Load the state dicts into the models
autoencoder.load_state_dict(autoencoder_load, strict=False)
teacher.load_state_dict(teacher_load, strict=False)
student.load_state_dict(student_load, strict=False)

# Set models to evaluation mode
autoencoder = autoencoder.eval()
teacher = teacher.eval()
student = student.eval()

# Move models to GPU if available and set to float32
if gpu:
    autoencoder = autoencoder.float().cuda()  # .half() 대신 .float() 사용
    teacher = teacher.float().cuda()
    student = student.float().cuda()

# Set the quantization multipliers (example values)
quant_mult = torch.e
quant_add = torch.pi

# 이미지 파일 경로 설정
image_path = "EfficientAD-main/error/quto1error.jpg"

# 이미지 불러오기
image = Image.open(image_path).convert("RGB")
transform = transforms.Compose([
    transforms.Resize((256, 256)),
    transforms.ToTensor(),
    transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225])
])
image_tensor = transform(image).unsqueeze(0)

# 이미지와 모델을 동일한 장치로 이동
if gpu:
    image_tensor = image_tensor.cuda()

# Perform inference
with torch.no_grad():
    # Forward pass through teacher and student networks
    if gpu:  # GPU 상에서 작업하는 경우, half precision 관련 코드를 제거하거나 변경
        teacher = teacher.float()  # .half() 대신 .float() 사용
        image_tensor = image_tensor.float()  # 입력 데이터를 float32로 변경
        teacher = teacher.cuda()  # 모델을 GPU로 이동

    t = teacher(image_tensor)
    s = student(image_tensor)

    # Calculate the discrepancy maps
    st_map = torch.mean((t - s[:, :384]) ** 2, dim=1)
    ae = autoencoder(image_tensor)
    
    ae_map = torch.mean((ae - s[:, 384:]) ** 2, dim=1)
    
    # Apply quantization
    st_map = st_map * quant_mult + quant_add
    ae_map = ae_map * quant_mult + quant_add
    
    # Combine the results
    result_map = st_map + ae_map
    result_on_cpu = result_map.cpu().numpy()

# 이미지의 판정 기준 설정 (임계값 예시)
threshold = 7.78

# 디스크리피언시 맵의 평균값 계산
mean_discrepancy = result_on_cpu.mean()

print(mean_discrepancy)

# 판정
if mean_discrepancy < threshold:
    print("정상")
else:
    print("불량")
    
import matplotlib.pyplot as plt

# 결과 맵 시각화
plt.figure(figsize=(10, 5))

# 원본 이미지 출력
plt.subplot(1, 3, 1)
plt.imshow(image)
plt.title('Original Image')
plt.axis('off')

# Teacher-Student Discrepancy Map 출력
plt.subplot(1, 3, 2)
st_map_cpu = st_map.cpu().squeeze().numpy()  # GPU를 사용하는 경우
plt.imshow(st_map_cpu, cmap='hot')
plt.title('Teacher-Student Discrepancy Map')
plt.axis('off')

# Autoencoder Discrepancy Map 출력
plt.subplot(1, 3, 3)
ae_map_cpu = ae_map.cpu().squeeze().numpy()  # GPU를 사용하는 경우
plt.imshow(ae_map_cpu, cmap='hot')
plt.title('Autoencoder Discrepancy Map')
plt.axis('off')

# 결과 맵 출력
plt.figure(figsize=(5, 5))
plt.imshow(result_on_cpu.squeeze(), cmap='hot')
plt.title('Final Anomaly Map')
plt.axis('off')

plt.show()