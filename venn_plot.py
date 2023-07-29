# !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
# File       : venn_plot.py
# Time       ：2022/6/2 9:28
# Author     ：Jago
# Email      ：18146856052@163.com
# version    ：python 3.7
# Description：
"""
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib_venn import venn3, venn2

# df1 = pd.read_excel("data/protein_0-2_with_ligands.xlsx", index_col=0)
# IDs1 = df1.index.tolist()
# df2 = pd.read_excel("data/DNA_0-2_with_ligands.xlsx", index_col=0)
# IDs2 = df2.index.tolist()
# df3 = pd.read_excel("data/RNA_0-2_with_ligands.xlsx", index_col=0)
# IDs3 = df3.index.tolist()
#
# plt.figure(figsize=(8, 8), dpi=100)
# g=venn3(subsets=[set(IDs1), set(IDs2), set(IDs3)], set_labels=('protein', 'DNA', 'RNA'))
# plt.show()

# df1 = pd.read_excel("data/pro(only)_0-2_with_ligands.xlsx", index_col=0)
# IDs1 = df1.index.tolist()
# df2 = pd.read_excel("data/NA(only)_0-2_with_ligands.xlsx", index_col=0)
# IDs2 = df2.index.tolist()
# df3 = pd.read_excel("data/pro+NA_0-2_with_ligands.xlsx", index_col=0)
# IDs3 = df3.index.tolist()
#
# plt.figure(figsize=(8, 8), dpi=100)
# g=venn3(subsets=[set(IDs1), set(IDs2), set(IDs3)], set_labels=('pro(only)', 'NA(only)', 'pro+NA'))
# plt.show()

# df1 = pd.read_excel("data/pro(only)_0-2_with_ligands.xlsx", index_col=0)
# IDs1 = df1.index.tolist()
# df2 = pd.read_excel("test/PDB_resolution_0-1.0A.xls", index_col=0)
# IDs2 = df2.index.tolist()
# df3 = pd.read_excel("test/PDB_resolution_1-1.5A.xls", index_col=0)
# IDs3 = df3.index.tolist()
#
# print(set(IDs2)-set(IDs1), set(IDs3)-set(IDs1))
# {nan, '4AYP'} {nan, '5YQW'} 这两个pdb中有糖
# plt.figure(figsize=(8, 8), dpi=100)
# g=venn3(subsets=[set(IDs1), set(IDs2), set(IDs3)], set_labels=('my_protein', 'v1_0-1_pro', 'v1_1-1.5_pro'))
# plt.show()

df1 = pd.read_excel("data/DNA_0-2_with_ligands.xlsx", index_col=0)
IDs1 = df1.index.tolist()
df2 = pd.read_excel("data/RNA_0-2_with_ligands.xlsx", index_col=0)
IDs2 = df2.index.tolist()
df3 = pd.read_excel("data/NA(only)_0-2_with_ligands.xlsx", index_col=0)
IDs3 = df3.index.tolist()

print(set(IDs2)-set(IDs1), set(IDs3)-set(IDs1))
plt.figure(figsize=(8, 8), dpi=100)
g = venn3(subsets=[set(IDs1), set(IDs2), set(IDs3)], set_labels=('my_DNA', 'my_RNA', 'NA(only)'))
plt.show()


