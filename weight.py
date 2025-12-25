import torch

weight_path = r"C:\Users\NguyenToan\pytorch-retinanet\resnet18-5c106cde.pth"

state_dict = torch.load(
    weight_path,
    map_location="cpu",
    weights_only=False   # 👈 FIX Ở ĐÂY
)

for name, tensor in state_dict.items():
    print(f"{name:40s} {tuple(tensor.shape)}")
