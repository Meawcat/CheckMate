import torch

print(torch.cuda.is_available()) # True면 활용 가능
print(torch.rand(5,3,device='cuda'))

print(f"PyTorch version: {torch.__version__}")
print(f"CUDA version: {torch.version.cuda}")
print(f"cuDNN version: {torch.backends.cudnn.version()}")