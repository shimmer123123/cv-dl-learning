"""
pytorch 综合练习
包括手动梯度下降 → nn.Module → DataLoader
"""

import torch
import torch.nn as nn
from torch.utils.data import Dataset, DataLoader


print(f"PyTorch 版本: {torch.__version__}")
print(f"CUDA 可用: {torch.cuda.is_available()}\n")


#Part 1: 手动梯度下降
print("=" * 50)
print("Part 1: 手动梯度下降（模拟 y = 2x")
print("=" * 50)

w = torch.tensor([1.0], requires_grad=True)
x_data = torch.tensor([1.0, 2.0, 3.0])
y_data = x_data * 2.0

for epoch in range(50):
    # 前向
    y_pred = w * x_data
    loss = ((y_pred - y_data) ** 2).mean()

    # 反向
    loss.backward()

    # 手动更新（注意用 .data 避免影响计算图）
    w.data -= 0.01 * w.grad.data

    # 清零梯度
    w.grad.zero_()

    if (epoch + 1) % 10 == 0:
        print(f"  Epoch {epoch+1:2d}, w={w.item():.4f}, loss={loss.item():.6f}")

print(f"最终 w ≈ {w.item():.4f}（目标 2.0）\n")


#Part 2: nn.Module 三层网络
print("=" * 50)
print("Part 2: nn.Module + 三层 MLP")
print("=" * 50)

class MLP(nn.Module):
    def __init__(self):
        super().__init__()
        self.net = nn.Sequential(
            nn.Linear(8, 6),
            nn.ReLU(),
            nn.Linear(6, 4),
            nn.ReLU(),
            nn.Linear(4, 1)
        )

    def forward(self, x):
        return self.net(x)


model = MLP()
criterion = nn.MSELoss()
optimizer = torch.optim.SGD(model.parameters(), lr=0.01)

# 造假数据
X = torch.randn(100, 8)
Y = torch.randn(100, 1)

for epoch in range(30):
    y_pred = model(X)
    loss = criterion(y_pred, Y)

    optimizer.zero_grad()
    loss.backward()
    optimizer.step()

    if (epoch + 1) % 10 == 0:
        print(f"  Epoch {epoch+1:2d}, loss={loss.item():.6f}")

print("MLP 训练完成\n")


#Part 3: Dataset + DataLoader
print("=" * 50)
print("Part 3: 自定义 Dataset + DataLoader")
print("=" * 50)

class DummyDataset(Dataset):
    def __init__(self, n_samples=200):
        self.x = torch.randn(n_samples, 8)
        self.y = torch.randn(n_samples, 1)

    def __len__(self):
        return len(self.x)

    def __getitem__(self, idx):
        return self.x[idx], self.y[idx]


dataset = DummyDataset(200)
dataloader = DataLoader(dataset, batch_size=16, shuffle=True)

print(f"数据集大小: {len(dataset)}")
print(f"Batch 大小: {dataloader.batch_size}")
print(f"总 Batch 数: {len(dataloader)}")

for batch_idx, (batch_x, batch_y) in enumerate(dataloader):
    # 模拟训练一步
    pred = model(batch_x)
    loss = criterion(pred, batch_y)

    if batch_idx == 0:
        print(f"\n第一个 Batch:")
        print(f"  x shape: {batch_x.shape}")   # [16, 8]
        print(f"  y shape: {batch_y.shape}")   # [16, 1]
        print(f"  pred shape: {pred.shape}")   # [16, 1]
        print(f"  loss: {loss.item():.6f}")

print("\nDataLoader 遍历完成")
print("\n04_pytorch_concepts.py 全部运行完成！")