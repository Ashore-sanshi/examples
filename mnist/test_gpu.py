import torch

print("torch版本：", torch.__version__)
print("cuda版本：", torch.version.cuda)
print("GPU是否可用：", torch.cuda.is_available())

if torch.cuda.is_available():
    print("GPU名称：", torch.cuda.get_device_name(0))
