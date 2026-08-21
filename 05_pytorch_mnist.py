"""
多分类（MNIST）完整训练脚本
Dataset/DataLoader + nn.Module + CrossEntropyLoss + SGD + 测试集准确率
GPU 自动切换、模型保存、训练/测试准确率打印
"""

import torch
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim
from torchvision import datasets, transforms
from torch.utils.data import DataLoader


#0. 设备
device = "cuda" if torch.cuda.is_available() else "cpu"
print(f"Using device: {device}")

#1. 数据
batch_size = 64
transform = transforms.Compose([
    transforms.ToTensor(),
    transforms.Normalize((0.1307,), (0.3081,))
])

train_dataset = datasets.MNIST(
    root="./data", train=True, download=True, transform=transform
)
test_dataset = datasets.MNIST(
    root="./data", train=False, download=True, transform=transform
)

train_loader = DataLoader(train_dataset, batch_size=batch_size, shuffle=True)
test_loader = DataLoader(test_dataset, batch_size=1000, shuffle=False)


#2. 模型
class Net(nn.Module):
    def __init__(self):
        super().__init__()
        self.l1 = nn.Linear(784, 512)
        self.l2 = nn.Linear(512, 256)
        self.l3 = nn.Linear(256, 128)
        self.l4 = nn.Linear(128, 64)
        self.l5 = nn.Linear(64, 10)

    def forward(self, x):
        x = x.view(-1, 784)          # 把 28x28 拉平
        x = F.relu(self.l1(x))
        x = F.relu(self.l2(x))
        x = F.relu(self.l3(x))
        x = F.relu(self.l4(x))
        return self.l5(x)            # 最后一层不接 softmax，CrossEntropy 内部包含


model = Net().to(device)
criterion = nn.CrossEntropyLoss()
optimizer = optim.SGD(model.parameters(), lr=0.01, momentum=0.5)


#3. 训练
def train(epoch):
    model.train()
    running_loss = 0.0
    for batch_idx, (inputs, target) in enumerate(train_loader):
        inputs, target = inputs.to(device), target.to(device)

        optimizer.zero_grad()
        outputs = model(inputs)
        loss = criterion(outputs, target)
        loss.backward()
        optimizer.step()

        running_loss += loss.item()
        if batch_idx % 300 == 299:
            print(f"[Epoch {epoch+1}, Batch {batch_idx+1}] loss: {running_loss/300:.4f}")
            running_loss = 0.0


#4. 测试
def test():
    model.eval()
    correct = 0
    total = 0
    with torch.no_grad():
        for images, labels in test_loader:
            images, labels = images.to(device), labels.to(device)
            outputs = model(images)
            _, predicted = torch.max(outputs.data, dim=1)
            total += labels.size(0)
            correct += (predicted == labels).sum().item()
    acc = 100 * correct / total
    print(f"Test set accuracy: {acc:.2f}%")
    return acc


#5. 主循环
if __name__ == "__main__":
    epochs = 3
    for epoch in range(epochs):
        train(epoch)
        test()

    # 保存模型权重
    torch.save(model.state_dict(), "mnist_model.pth")
    print("模型已保存为 mnist_model.pth")
    print("05_pytorch_mnist.py 运行完成！")