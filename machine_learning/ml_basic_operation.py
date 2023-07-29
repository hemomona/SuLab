# !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
# File       : ml_basic_operation.py
# Time       ：2022/6/10 11:12
# Author     ：Jago
# Email      ：18146856052@163.com
# version    ：python 3.7
# Description：
"""
import math

import numpy as np
import matplotlib.pyplot as plt

# # 建立矩阵
# A = np.mat([[1, 2], [3, 4], [5, 6]])
# print(A)
#
# # 建立特殊矩阵
# A = np.ones((2, 3))
# print(A)
# B = np.zeros((2, 3))
# print(B)
# I = np.eye(6)
# print(I)
#
# C = np.random.rand(3, 3)
# print(C)
# D = np.random.randn(1, 3)
# print(D)

# # 矩阵大小
# A = np.mat([[1, 2], [3, 4], [5, 6]])
# print("矩阵A的大小： ", A.shape)
# print("矩阵A的行数： ", A.shape[0])
# print("矩阵A的列数： ", A.shape[1])
#
# V = np.mat([1, 2, 3, 4])
# print("矩阵V的最大维度为： ", max(V.shape))
#
# # 操作数据
# A = np.mat([[1, 2], [3, 4], [5, 6]])
# print(A[2, 1])          # 索引为（2,1）的值
# print(A[1, :])          # 第二行所有元素
# print(A[:, 1])          # 第二列所有元素
#
# A[:, 1] = [[1], [2], [3]]      # 把第二列替换掉
# B = [[10], [11], [12]]
# C = [[10, 11]]
# print(np.c_[A, B])             # 为矩阵加上列
# print(np.r_[A, C])             # 为矩阵加上行

# A = np.mat([[1, 2], [3, 4], [5, 6]])
# B = np.ones((3, 2))
# C = np.mat([[1, 1], [2, 2]])
#
# print("A*C = ", np.dot(A, C))        # 内积
# print("A*B = ", np.multiply(A, B))  # 对应元素相乘
# print(A+1)
#
# # 转置和逆
# print("矩阵A的转置： ", A.T)
# print("矩阵A的逆为： ", A.I)
#
# print("矩阵A的最大值： ", np.max(A))
# print("矩阵A各元素之和： ", np.sum(A))

# t = np.arange(0, 0.98, 0.01)
#
# y1 = np.sin(2*math.pi*4*t)
# y2 = np.cos(2*math.pi*4*t)
#
# plt.plot(t, y1)
# plt.plot(t, y2)
#
# plt.xlabel('time')                  # 横坐标
# plt.ylabel('value')                 # 纵坐标
# plt.legend(['sin', 'cos'])          # 标注名称
# plt.title('myplot')                 # 标题
#
# plt.show()


def cost_function(X, y, theta):
    m = X.shape[0]
    predictions = X*theta
    cost = predictions - y
    sqrErrors = [[cost[i][j] ** 2 for j in range(len(cost[i]))] for i in range(len(cost))]

    J = 1/(2*m)*np.sum(sqrErrors)
    return J


# 给出例子
X = np.mat([[1, 1], [1, 2], [1, 3]])
y = np.mat([[1], [2], [3]])
theta = np.mat([[0], [0]])

print("代价函数的结果的为 ", cost_function(X, y, theta))
