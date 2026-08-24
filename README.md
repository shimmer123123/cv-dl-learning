# CV/DL Learning Notes

>华南理工大学软件学院 2025 级本科生
>
>自学计算机视觉与深度学习基础（Python → NumPy → OpenCV → PyTorch）

## 仓库说明

本仓库记录了从零开始学习 CV/DL 基础工具链的过程，包含 7 个脚本，环境配置正确后即可运行。

## 环境依赖

```bash
pip install numpy opencv-python torch torchvision matplotlib -i https://pypi.tuna.tsinghua.edu.cn/simple
```
Python 3.9+ 推荐。

## 脚本说明

| 文件 | 内容 |
|---|---|
| 01_python_basics.py | 变量、列表/字典、循环、函数、文件读写、异常处理 |
| 02_numpy_demo.py | 数组创建、reshape、切片、运算、矩阵乘法、统计 |
| 03_opencv_demo.py | 图像读取、灰度化、resize、ROI 裁剪与保存 |
| 04_pytorch_concepts.py | Tensor 自动求导 + nn.Module 模型构建 + DataLoader 数据加载 |
| 05_pytorch_mnist.py | MNIST 手写数字分类完整训练（3 Epoch，支持 GPU） |
| 06_pytorch_fashion-mnist.py | Fashion-MNIST 数据集训练与基础模型评估 |
| 07_pytorch_mnist_CNN.ipynb | 基于 CNN 的手写数字识别（Jupyter Notebook） |

## 运行方式

```bash
python 01_python_basics.py
python 02_numpy_demo.py
python 03_opencv_demo.py # 需在同目录放一张 test.jpg
python 04_pytorch_concepts.py
python 05_pytorch_mnist.py # 首次运行自动下载 MNIST 数据集
python 06_pytorch_fashion-mnist.py  # 首次运行自动下载 Fashion-MNIST 数据集
# 07_pytorch_mnist_CNN.ipynb 请在 Jupyter Notebook 或 JupyterLab 中打开运行
```
## 学习状态

- [x] Python 基础语法
- [x] NumPy 数组操作
- [x] OpenCV 图像读取与预处理
- [x] PyTorch 训练流程跑通
- [x] Fashion-MNIST 基础训练
- [x] CNN 卷积神经网络入门
- [ ] 后续：进组后继续深入数据处理与实验跑通

## 联系方式

邮箱：202530550112@mail.scut.edu.cn
