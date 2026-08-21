"""
NumPy 基础练习
包括数组创建、属性、索引切片、形状操作、数学运算、统计、矩阵乘法
"""

import numpy as np


#1. 数组创建
print("1. 数组创建")

a = np.array([1, 2, 3, 4, 5])
print(f"一维数组 a: {a}, 形状: {a.shape}, 数据类型: {a.dtype}")

b = np.zeros((3, 4))
print(f"\n全零矩阵 (3x4):\n{b}")

c = np.ones((2, 3))
print(f"\n全一矩阵 (2x3):\n{c}")

d = np.arange(0, 12, 2)  # 0,2,4,6,8,10
print(f"\narange(0,12,2): {d}")

e = np.linspace(0, 1, 5)  # 0到1均匀5个数
print(f"linspace(0,1,5): {e}")

f = np.random.randn(3, 3)  # 随机正态分布
print(f"\n随机矩阵 (3x3):\n{f}")


#2. 数组属性
print("\n2. 数组属性")
print(f"维度数: {f.ndim}")
print(f"形状: {f.shape}")
print(f"元素总数: {f.size}")
print(f"每个元素字节数: {f.itemsize}")


#3. 索引与切片
print("\n3. 索引与切片")

g = np.arange(1, 13).reshape(3, 4)
print(f"原始矩阵 (3x4):\n{g}")

print(f"\n取第 0 行: {g[0]}")
print(f"取第 2 列: {g[:, 2]}")
print(f"取 2x2 子矩阵:\n{g[:2, :2]}")
print(f"条件筛选 (>6): {g[g > 6]}")


#4. 形状操作
print("\n4. 形状操作")

h = np.arange(12)
print(f"\n一维 (12,): {h}")

h_reshaped = h.reshape(3, 4)
print(f"reshape 为 (3,4):\n{h_reshaped}")

h_flattened = h_reshaped.flatten()
print(f"flatten 回一维: {h_flattened}")

h_transposed = h_reshaped.T
print(f"\n转置后 (4x3):\n{h_transposed}")


#5. 数学运算
print("\n5. 数学运算")

x = np.array([1, 2, 3])
y = np.array([4, 5, 6])

print(f"x = {x}")
print(f"y = {y}")
print(f"x + y = {x + y}")
print(f"x * y = {x * y}")       # 逐元素相乘
print(f"x ** 2 = {x ** 2}")
print(f"np.dot(x, y) = {np.dot(x, y)}")  # 点积 = 1 * 4+2 * 5+3 * 6 = 32
print(f"np.sqrt(x) = {np.sqrt(x)}")


#6. 统计函数
print("\n6. 统计函数")

data = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(f"数据:\n{data}")
print(f"均值: {data.mean():.2f}")
print(f"按列均值: {data.mean(axis=0)}")
print(f"按行均值: {data.mean(axis=1)}")
print(f"最大值: {data.max()}")
print(f"最小值: {data.min()}")
print(f"标准差: {data.std():.2f}")
print(f"求和: {data.sum()}")


#7. 矩阵乘法（深度学习核心）
print("\n7. 矩阵乘法")

A = np.array([[1, 2], [3, 4]])       # (2,2)
B = np.array([[5, 6], [7, 8]])       # (2,2)

C = np.dot(A, B)                      # 矩阵乘法
print(f"A:\n{A}")
print(f"B:\n{B}")
print(f"A @ B =\n{C}")

# 验证: A的第一行 [1,2] 点乘 B的第一列 [5,7] = 1 * 5+2 * 7 = 19
print(f"\n验证 C[0,0] = 1 * 5 + 2 * 7 = 19 ✓")


#8. 广播机制
print("\n8. 广播机制")

M = np.array([[1, 2, 3], [4, 5, 6]])   # (2,3)
v = np.array([10, 20, 30])              # (3,)

result = M + v                          # v 广播到每一行
print(f"M:\n{M}")
print(f"v: {v}")
print(f"M + v (广播):\n{result}")


print("\n02_numpy_demo.py 全部运行完成！")