# !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
# File       : clean_allions.py
# Time       ：2022/6/3 17:09
# Author     ：Jago
# Email      ：18146856052@163.com
# version    ：python 3.7
# Description：
"""
import pandas as pd

ion_path = "data/ions.txt"
xlsx_path = "data/pro(only)_0-2_with_ligands.xlsx"
save_path = "data/pro(only)_0-2_with_ligands_with_nonions.xlsx"

f = open(ion_path)
ions = []
for line in f.readlines():
    ions.append(line.strip('\n'))
f.close()

df = pd.read_excel(xlsx_path, index_col=0)
IDs = df.index.tolist()

print("***start process***")
for id in IDs:
    ligands = str(df.at[id, 'Unique Ligands'])
    ligands_list = ligands.split(',')

    ligands_list_new = []
    for l in ligands_list:
        ligands_list_new.append(l.strip())

    if all(l in ions for l in ligands_list_new):
        print("drop ", id)
        df.drop(id, inplace=True)

df.to_excel(save_path)
print("***finish process***")
