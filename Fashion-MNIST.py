import torch
import torch.nn as nn
import torch.optim as optim
from torchvision import datasets,transforms
from torch.utils.data import DataLoader
import torch.nn.functional as F

print("PyTorch version:",torch.__version__)
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
print("Device:", device)

transform_train = transforms.Compose([
    transforms.RandomHorizontalFlip(),   # 随机水平翻转
    transforms.RandomRotation(10),       # 随机旋转 ±10 度
    transforms.ToTensor(),
    transforms.Normalize((0.5,), (0.5,))
])

transform_test = transforms.Compose([
    transforms.ToTensor(),
    transforms.Normalize((0.5,), (0.5,))
])

train_dataset=datasets.FashionMNIST(
    root="./data",
    train=True,
    download=True,
    transform=transform_train
)

test_dataset=datasets.FashionMNIST(
    root="./data",
    train=False,
    download=True,
    transform=transform_test 
)

train_loader=DataLoader(train_dataset,batch_size=64,shuffle=True)
test_loader=DataLoader(test_dataset,batch_size=1000,shuffle=False)

class Net(nn.Module):
    def __init__(self):
        super(Net, self).__init__()
        # 卷积层1：1 → 64
        self.conv1 = nn.Conv2d(1, 64, kernel_size=3, padding=1)
        self.bn1 = nn.BatchNorm2d(64)
        # 卷积层2：64 → 128
        self.conv2 = nn.Conv2d(64, 128, kernel_size=3, padding=1)
        self.bn2 = nn.BatchNorm2d(128)
        # 卷积层3（新增）：128 → 128
        self.conv3 = nn.Conv2d(128, 128, kernel_size=3, padding=1)
        self.bn3 = nn.BatchNorm2d(128)
        
        self.pool = nn.MaxPool2d(2, 2)
        
        # 全连接层：128通道 × 7×7 = 6272 → 256 → 10
        self.fc1 = nn.Linear(128 * 7 * 7, 256)
        self.fc2 = nn.Linear(256, 10)
        self.dropout = nn.Dropout(0.3) # 稍微降低一点dropout率

    def forward(self, x):
        x = self.pool(F.relu(self.bn1(self.conv1(x))))  # 28→14
        x = self.pool(F.relu(self.bn2(self.conv2(x))))  # 14→7
        x = F.relu(self.bn3(self.conv3(x)))             # 7×7 卷积，尺寸不变，加深特征
        x = x.view(-1, 128 * 7 * 7)                     # 拉平
        x = F.relu(self.fc1(x))
        x = self.dropout(x)
        x = self.fc2(x)
        return x

model=Net().to(device)

criterion=nn.CrossEntropyLoss()
optimizer=optim.Adam(model.parameters(), lr=0.001)
scheduler = optim.lr_scheduler.StepLR(optimizer, step_size=5, gamma=0.5)


def train(epoch):
    model.train()
    running_loss=0.0
    for batch_idx,(inputs,target)in enumerate(train_loader):
        inputs,target=inputs.to(device),target.to(device)
        optimizer.zero_grad()
        outputs=model(inputs)
        loss=criterion(outputs,target)
        loss.backward()
        optimizer.step()
        running_loss+=loss.item()
        if batch_idx%300==299:
            print(f"[Epoch {epoch+1}, Batch {batch_idx+1}] loss: {running_loss/300:.4f}")
            running_loss = 0.0


def test():
    model.eval()
    correct=0
    total=0
    with torch.no_grad():
        for images,labels in test_loader:
            images,labels=images.to(device),labels.to(device)
            outputs=model(images)
            _,predicted=torch.max(outputs.data,dim=1)
            total+=labels.size(0)
            correct+=(predicted==labels).sum().item()
    acc=100*correct/total
    print(f"  测试集准确率: {acc:.2f}%")

if __name__=="__main__":
    epochs=20
    for epoch in range(epochs):
        train(epoch)
        test()
        scheduler.step()   
    torch.save(model.state_dict(),"fashion_mnist_model.pth")
    print("模型已保存为 fashion_mnist_model.pth")


