# !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
# File       : venn_test1.py
# Time       ：2022/6/1 19:31
# Author     ：Jago
# Email      ：18146856052@163.com
# version    ：python 3.7
# Description：
"""
import pandas as pd

'''df1 = pd.read_excel("data/NA(only)_0-2_with_ligands.xlsx", index_col=0)
IDs1 = df1.index.tolist()
df2 = pd.read_excel("data/DNA_0-2_with_ligands.xlsx", index_col=0)
IDs2 = df2.index.tolist()
df3 = pd.read_excel("data/RNA_0-2_with_ligands.xlsx", index_col=0)
IDs3 = df3.index.tolist()

set1 = set(IDs1)
set2 = set(IDs2)
set3 = set(IDs3)

print(set1 & set2 & set3)'''
# {'4U6M', '7BPG', '7A9L', '6ZR1', '1PJO', '6ZPF', '6ZWU', '6ZRL', '1G4Q', '4U6L', '6ZX5', '4U6K', '7A9O', '6ZX8', '421D', '7THB', '6ZRS', '1PJG', '7A9N', '6ZQ9', '2DQQ', '7A9P', '7A9T', '479D', '7BPV', '6ZW3', '3SSF'}

# df1 = pd.read_excel("data/protein_0-2_with_ligands.xlsx", index_col=0)
# IDs1 = df1.index.tolist()
# df2 = pd.read_excel("data/DNA_0-2_with_ligands.xlsx", index_col=0)
# IDs2 = df2.index.tolist()
# df3 = pd.read_excel("data/RNA_0-2_with_ligands.xlsx", index_col=0)
# IDs3 = df3.index.tolist()
#
# set1 = set(IDs1)
# set2 = set(IDs2)
# set3 = set(IDs3)
# set4 = set1 & (set2 | set3)
#
# # print(len(set4), ": ", set4)
# # 1815 :  {'2VJV', '3M7K', '5KG5', '1YTB', '6CTN', '4QVD', ...} 就是说从之前的数据集可以导出1815个pro+NA
# df4 = pd.read_excel("data/pro+NA_0-2_with_ligands.xlsx", index_col=0)
# IDs4 = df4.index.tolist()  # 1787条
# # i = 0
# # for id in IDs4:
# #     if id not in set4:  # set4是pro & (DNA | RNA)的集合
# #         i += 1
# #         print(id)
# # print("find ", i)
# # find 20 1QNE 2Y8Y 3KJO 3PVV 4PUQ 4WB3 5EV2 5EV3 5EV4 5USB 5USN 5USO 5Z4A 5Z4D 6E4P 6OZF 6OZG 6OZN 7P9I 7TZV
# # 就是说有20个下载的pro+NA不在导出的
#
# set5 = set4 - set(IDs4)
# print(len(set5), set5)
# # 48 {'4YFU', '3EZ5', '2HW3', '3TAP', '2HHS', '1P71', '5HRT', '3TAN', '1NK0', '4F2S', '4F2R', '4B9S', '1L3T', '2HHW', '1NK8', '1L3U', '2HHV', '1NKC', '1L3S', '2HHU', '1NK7', '1NJW', '3HP6', '1OWF', '1L3V', '1NKE', '1NJZ', '3WPC', '1NJY', '2HHQ', '1U47', '1NK9', '1XC9', '1NK4', '2HVI', '1NKB', '1NJX', '1U4B', '3HT3', '6YRQ', '3TAR', '5Y3J', '4UQG', '4QVI', '6UEU', '3TAQ', '1L5U', '3HPO'}
# # 就是说有48个导出的不在下载的，查询后发现都有糖

# df1 = pd.read_excel("data/protein_0-2_with_ligands.xlsx", index_col=0)
# IDs1 = df1.index.tolist()
# set1 = set(IDs1)
# df2 = pd.read_excel("data/pro(only)_0-2_with_ligands.xlsx", index_col=0)
# IDs2 = df2.index.tolist()
# set2 = set(IDs2)
# df3 = pd.read_excel("data/pro+NA_0-2_with_ligands.xlsx", index_col=0)
# IDs3 = df3.index.tolist()
# set3 = set(IDs3)
# set4 = set1 - set2 - set3  # pro+other
#
# data = []
# for id in set4:
#     row = [id] + list(df1.loc[id])
#     data.append(row)
#
# df = pd.DataFrame(data, columns=['ID', 'href', 'Macromolecule', 'Released', 'Method', 'Resolution', 'Organisms',
#                                  'Unique Ligands', 'Unique branched monosaccharides'])
# df.to_excel("data/pro+other_0-2_with_ligands.xlsx", index=False)
# print("***extract ", len(data), " records***")

# df1 = pd.read_excel("data/RNA_0-2_with_ligands.xlsx", index_col=0)
# IDs1 = df1.index.tolist()
# set1 = set(IDs1)
# df2 = pd.read_excel("data/pro+NA_0-2_with_ligands.xlsx", index_col=0)
# IDs2 = df2.index.tolist()
# set2 = set(IDs2)
# # df3 = pd.read_excel("data/pro+NA_0-2_with_ligands.xlsx", index_col=0)
# # IDs3 = df3.index.tolist()
# # set3 = set(IDs3)
# set4 = set1 & set2  # RNA+other
#
# data = []
# for id in set4:
#     row = [id] + list(df1.loc[id])
#     data.append(row)
#
# df = pd.DataFrame(data, columns=['ID', 'href', 'Macromolecule', 'Released', 'Method', 'Resolution', 'Organisms',
#                                  'Unique Ligands', 'Unique branched monosaccharides'])
# df.to_excel("data/pro+RNA_0-2_with_ligands.xlsx", index=False)
# print("***extract ", len(data), " records***")

df1 = pd.read_excel("data/DNA_0-2_with_ligands.xlsx", index_col=0)
IDs1 = df1.index.tolist()
set1 = set(IDs1)
df2 = pd.read_excel("data/RNA_0-2_with_ligands.xlsx", index_col=0)
IDs2 = df2.index.tolist()
set2 = set(IDs2)
df3 = pd.read_excel("data/NA(only)_0-2_with_ligands.xlsx", index_col=0)
IDs3 = df3.index.tolist()
set3 = set(IDs3)


print(len(set1 - set2 - set3), set1 - set2 - set3)
print(len(set1 & set3 - set2), set1 & set2 - set3)
print(len(set2 - set1 - set3), set2 - set1 - set3)
print(len(set2 & set3 - set1), set2 & set3 - set1)
print(len(set3 - set1 - set2), set3 - set1 - set2)
print(len(set3 & set1 & set2), set3 & set1 & set2)
