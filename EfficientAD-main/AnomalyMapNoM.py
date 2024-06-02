#!/usr/bin/python
# -*- coding: utf-8 -*-
import numpy as np
import torch
from torch import nn
import os
from torchvision import transforms
from PIL import Image
import glob
import matplotlib.pyplot as plt
import tifffile
from tqdm import tqdm
import argparse


# 현재 스크립트 파일의 절대 경로를 가져옵니다.
script_path = os.path.abspath(__file__)

# 스크립트 파일이 있는 디렉토리 경로를 가져옵니다.
script_dir = os.path.dirname(script_path)

# 작업 디렉토리를 스크립트 파일이 있는 디렉토리로 변경합니다.
os.chdir(script_dir)

# Define argparse
def get_argparse():
    parser = argparse.ArgumentParser()
    parser.add_argument('-t', '--threshold', type=float, default=0, help='Threshold for anomaly detection')
    parser.add_argument('-i', '--image_dir', required=True, help='Relative path to the image directory')
    parser.add_argument('-d', '--model_dir', required=True, help='Relative path to the image directory')
    parser.add_argument('-o', '--output_dir', default=None, help='Download path to the image directory')
    return parser.parse_args()

# Parse arguments
args = get_argparse()

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
on_gpu = torch.cuda.is_available()

# Initialize the models
autoencoder = get_ae()
teacher = get_pdn(384)
student = get_pdn(768)

# Load trained model weights
auto_dir = args.model_dir
teach_dir = args.model_dir
stu_dir = args.model_dir #'output/erazer_model/trainings/mvtec_ad/erazer'
autoencoder_load = torch.load(os.path.join(auto_dir, 'autoencoder_tmp.pth'))
teacher_load = torch.load(os.path.join(teach_dir, 'teacher_tmp.pth'))
student_load = torch.load(os.path.join(stu_dir, 'student_tmp.pth'))

# Load the state dicts into the models
autoencoder.load_state_dict(autoencoder_load, strict=False)
teacher.load_state_dict(teacher_load, strict=False)
student.load_state_dict(student_load, strict=False)

# Set models to evaluation mode
autoencoder = autoencoder.eval()
teacher = teacher.eval()
student = student.eval()

# Move models to GPU if available and set to float32
if on_gpu:
    autoencoder = autoencoder.float().cuda()
    teacher = teacher.float().cuda()
    student = student.float().cuda()

# Define the image transform
default_transform = transforms.Compose([
    transforms.Resize((256, 256)),
    transforms.ToTensor(),
    transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225])
])

# Define the predict function
@torch.no_grad()
def predict(image, teacher, student, autoencoder, teacher_mean, teacher_std,
            q_st_start=None, q_st_end=None, q_ae_start=None, q_ae_end=None):
    teacher_output = teacher(image)
    teacher_output = (teacher_output - teacher_mean) / teacher_std
    student_output = student(image)
    autoencoder_output = autoencoder(image)
    map_st = torch.mean((teacher_output - student_output[:, :384])**2, dim=1, keepdim=True)
    map_ae = torch.mean((autoencoder_output - student_output[:, 384:])**2, dim=1, keepdim=True)
    if q_st_start is not None:
        map_st = 0.1 * (map_st - q_st_start) / (q_st_end - q_st_start)
    if q_ae_start is not None:
        map_ae = 0.1 * (map_ae - q_ae_start) / (q_ae_end - q_ae_start)
    map_combined = 0.5 * map_st + 0.5 * map_ae
    return map_combined, map_st, map_ae

# 이미지 파일 경로 설정
#image_list = glob.glob('C:/Users/Me/Downloads/4-1/MJU_CheckMate/MJU_CheckMate/EfficientAD-main/mvtec_anomaly_detection/erazer/test/good/*.jpg')
#image_list = glob.glob('C:/Users/Me/Downloads/4-1/MJU_CheckMate/MJU_CheckMate/EfficientAD-main/error/*.jpg')
# 이미지 파일 또는 디렉토리 경로 가져오기
if args.image_dir.endswith('.jpg'):
    # 이미지 파일 경로로 간주
    image_list = [args.image_dir]
else:
    # 디렉토리 내의 이미지 파일 경로로 간주
    image_list = glob.glob(os.path.join(args.image_dir, '*.jpg'))

# 임계값 설정
threshold = args.threshold

# Process each image and generate anomaly maps
for image_path in image_list:
    # Load and preprocess the image
    image = Image.open(image_path).convert("RGB")
    image_tensor = default_transform(image).unsqueeze(0)

    if on_gpu:
        image_tensor = image_tensor.cuda()

    with torch.no_grad():
        # Perform prediction
        map_combined, map_st, map_ae = predict(
            image=image_tensor, teacher=teacher, student=student,
            autoencoder=autoencoder, teacher_mean=0,
            teacher_std=1)

        # Process the combined map
        orig_width, orig_height = image.size
        map_combined = torch.nn.functional.pad(map_combined, (4, 4, 4, 4))
        map_combined = torch.nn.functional.interpolate(
            map_combined, (orig_height, orig_width), mode='bilinear')
        map_combined = map_combined[0, 0].cpu().numpy()

        # Anomaly detection
        mean_value = map_ae.mean()
        is_anomaly = mean_value > threshold
        
        if is_anomaly:
            is_anomaly = '불량'
        else:
            is_anomaly = '정상'
        
    # # 시각화
    # plt.figure(figsize=(10, 5))

    # # 원본 이미지 출력
    # plt.subplot(1, 3, 1)
    # plt.imshow(image)
    # plt.title('Original Image')
    # plt.axis('off')

    # # Autoencoder Discrepancy Map 출력
    # plt.subplot(1, 3, 3)
    # plt.imshow(map_ae[0, 0].cpu().numpy(), cmap='hot')
    # print(f'Discrepancy Map Mean: {map_ae.mean().item()}')
    # plt.title('Autoencoder Discrepancy Map')
    # plt.axis('off')

    # 이상 탐지 결과 출력
    print(f'[Image: {image_path}]||[Anomaly Detected: {is_anomaly}]||[Mean Value: {mean_value}]')
    
    # 이상 탐지 결과 저장
    if args.output_dir != None:
        base_name = os.path.basename(image_path)
        file_name = os.path.splitext(base_name)[0] + "_anomaly.jpg"
        
        output_file = os.path.join(args.output_dir, file_name)
        plt.imshow(map_ae[0, 0].cpu().numpy(), cmap='hot')
        plt.axis('off')
        plt.savefig(output_file, bbox_inches='tight', pad_inches=0)
        plt.close()

    plt.show()
    