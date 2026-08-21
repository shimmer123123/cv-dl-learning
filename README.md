\# CV/DL Learning Notes



> 华南理工大学软件学院 2025 级本科生  

> 自学计算机视觉与深度学习基础（Python → NumPy → OpenCV → PyTorch）



\## 仓库说明



本仓库记录了我从零开始学习 CV/DL 基础工具链的过程，包含 5 个脚本，均可在本地直接运行。



\## 环境依赖



```bash
pip install numpy opencv-python torch torchvision matplotlib
```​


Python 3.9+ 推荐。



\## 脚本说明



| 文件 | 内容 |

|---|---|

| `01\_python\_basics.py` | 变量、列表/字典、循环、函数、文件读写、异常处理 |

| `02\_numpy\_demo.py` | 数组创建、reshape、切片、运算、矩阵乘法、统计 |

| `03\_opencv\_demo.py` | 读图 → 灰度 → resize → 保存 |

| `04\_pytorch\_concepts.py` | 手动梯度下降 + nn.Module + DataLoader |

| `05\_pytorch\_mnist.py` | MNIST 完整训练（3 epoch，可 GPU） |



\## 运行方式


```​
bash

python 01\_python\_basics.py

python 02\_numpy\_demo.py

python 03\_opencv\_demo.py # 需在同目录放一张 test.jpg

python 04\_pytorch\_concepts.py

python 05\_pytorch\_mnist.py # 首次运行自动下载 MNIST 数据集
```​


\## 学习状态



\- \[x] Python 基础语法（黑马，前 30 集）

\- \[x] NumPy 数组操作（尚硅谷，006\~021）

\- \[x] OpenCV 图像读取与预处理（唐宇迪，前 4 小时）

\- \[x] PyTorch 训练流程跑通（刘二大人 P1\~P8）

\- \[ ] 后续：进组后继续深入数据处理与实验跑通



\## 联系方式



Email: 202530550112@mail.scut.edu.cn

