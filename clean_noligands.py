# !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
# File       : clean_noligands.py
# Time       ：2022/6/1 18:27
# Author     ：Jago
# Email      ：18146856052@163.com
# version    ：python 3.7
# Description：
"""
import pandas as pd

xlsx_path = "data/pro(only)_0-2_raw.xlsx"
save_path = "data/pro(only)_0-2_with_ligands.xlsx"

df = pd.read_excel(xlsx_path, index_col=0)
IDs = df.index.tolist()

print("***start process***")
for id in IDs:
    if str(df.at[id, 'Unique Ligands']) == "  ":
        print("drop ", id)
        df.drop(id, inplace=True)

df.to_excel(save_path)
print("***finish process***")
