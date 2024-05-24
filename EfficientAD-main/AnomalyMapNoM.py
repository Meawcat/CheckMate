#!/usr/bin/python
# -*- coding: utf-8 -*-
import numpy as np
import torch
from torch import nn
import os
from torchvision import transforms
from PIL import Image

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
auto_dir = 'output/hyotto_model_small/trainings/mvtec_ad/hyotto'
teach_dir = 'output/hyotto_model_small/trainings/mvtec_ad/hyotto'
stu_dir = 'output/hyotto_model_small/trainings/mvtec_ad/hyotto'
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
    autoencoder = autoencoder.float().cuda()
    teacher = teacher.float().cuda()
    student = student.float().cuda()

# Define functions for p-quantiles and normalization
def calculate_p_quantiles(anomaly_scores, qa_quantile=0.9, qb_quantile=0.995):
    qa = np.quantile(anomaly_scores, qa_quantile)
    qb = np.quantile(anomaly_scores, qb_quantile)
    return qa, qb

def normalize_anomaly_map(anomaly_map, qa, qb):
    normalized_map = np.clip((anomaly_map - qa) / (qb - qa), 0, 1)
    return normalized_map

def average_maps(local_map, global_map):
    return (local_map + global_map) / 2

# 이미지 파일 경로 설정
validation_image_paths = [
    "error/051.jpg",
    "error/050.jpg",
    # ... 더 많은 정상 이미지 경로
]

test_image_paths = [
    "error/052.jpg",  # 정상 이미지
    "error/034.jpg",  # 불량 이미지
    # ... 더 많은 정상 및 불량 이미지 경로
]

# 이미지 전처리 함수
transform = transforms.Compose([
    transforms.Resize((384, 384)),
    transforms.ToTensor(),
    transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225])
])

# Validation 이미지의 anomaly scores 계산
validation_local_scores = []
validation_global_scores = []

for image_path in validation_image_paths:
    image = Image.open(image_path).convert("RGB")
    image_tensor = transform(image).unsqueeze(0)
    if gpu:
        image_tensor = image_tensor.cuda()

    with torch.no_grad():
        
        print(f"Input tensor shape: {image_tensor.shape}")
        
        # Autoencoder를 통한 global anomaly score 계산
        ae_output = autoencoder(image_tensor)
        print(f"Autoencoder output shape: {ae_output.shape}")
        
        # Reshape or upsample autoencoder output if sizes don't match
        if ae_output.shape != image_tensor.shape:
            ae_output = torch.nn.functional.interpolate(ae_output, size=image_tensor.shape[2:], mode='bilinear', align_corners=False)
            print(f"Resized Autoencoder output shape: {ae_output.shape}")
            
        # Adjust channel dimension if necessary
        if ae_output.shape[1] != image_tensor.shape[1]:
            ae_output = ae_output.permute(0, 2, 3, 1)
            ae_output = ae_output.reshape(-1, image_tensor.shape[2], image_tensor.shape[3], 3)
            ae_output = ae_output.permute(0, 3, 1, 2)
            print(f"Adjusted Autoencoder output shape: {ae_output.shape}")
        
        global_anomaly_score = torch.mean((image_tensor - ae_output) ** 2).item()
        validation_global_scores.append(global_anomaly_score)

        # Teacher, Student 네트워크를 통한 local anomaly score 계산
        teacher_output = teacher(image_tensor)
        student_output = student(image_tensor)
        print(teacher)
        print(student)
        local_anomaly_score = torch.mean((teacher_output - student_output) ** 2).item()
        validation_local_scores.append(local_anomaly_score)

validation_local_scores = np.array(validation_local_scores)
validation_global_scores = np.array(validation_global_scores)

# Validation 이미지를 기반으로 p-quantiles 계산
qa_local, qb_local = calculate_p_quantiles(validation_local_scores)
qa_global, qb_global = calculate_p_quantiles(validation_global_scores)

# Test 이미지의 anomaly map 계산 및 정규화
test_local_scores = []
test_global_scores = []

for image_path in test_image_paths:
    image = Image.open(image_path).convert("RGB")
    image_tensor = transform(image).unsqueeze(0)
    if gpu:
        image_tensor = image_tensor.cuda()

    with torch.no_grad():
        # Autoencoder를 통한 global anomaly score 계산
        ae_output = autoencoder(image_tensor)
        global_anomaly_score = torch.mean((image_tensor - ae_output) ** 2).item()
        test_global_scores.append(global_anomaly_score)

        # Teacher, Student 네트워크를 통한 local anomaly score 계산
        teacher_output = teacher(image_tensor)
        student_output = student(image_tensor)
        local_anomaly_score = torch.mean((teacher_output - student_output) ** 2).item()
        test_local_scores.append(local_anomaly_score)

test_local_scores = np.array(test_local_scores)
test_global_scores = np.array(test_global_scores)

# Test 이미지의 anomaly map 정규화 및 평균화
normalized_local_maps = [normalize_anomaly_map(score, qa_local, qb_local) for score in test_local_scores]
normalized_global_maps = [normalize_anomaly_map(score, qa_global, qb_global) for score in test_global_scores]
final_anomaly_maps = [average_maps(local, global_map) for local, global_map in zip(normalized_local_maps, normalized_global_maps)]

# Test 이미지의 최종 anomaly maps 출력
for i, anomaly_map in enumerate(final_anomaly_maps):
    print(f"Test Image {i+1}: Anomaly Score: {anomaly_map}")