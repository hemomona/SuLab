# !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
# File       : clean_illegal_ligands.py
# Time       ：2022/6/11 11:14
# Author     ：Jago
# Email      ：18146856052@163.com
# version    ：python 3.7
# Description：
"""
import re

import pandas as pd

# csv_file = "data/all_ligands.csv"
# save_file = "data/illegal_ligands_id.txt"
#
# legal_elements = ['C', 'N', 'O', 'H', 'P', 'S', 'F', 'CL', 'BR', 'I', 'AT', 'TS']
#
# df = pd.read_csv(csv_file)
#
# print("***start process***")
# with open(save_file, 'a') as f:
#     for index, row in df.iterrows():
#         id = str(row['ID'])
#         weight = str(row['Molecular Weight']).replace(',', '')
#         weight = float(weight)
#         formula = str(row['Formula'])
#
#         try:
#             if weight >= 1000:
#                 f.write(id + '\n')
#                 continue
#
#             elements = re.sub(r'[0-9]+', '', formula).split()
#
#             if 'C' not in elements:  # 如果formula不包括C，就continue，继续外部循环
#                 f.write(id + '\n')
#                 continue
#
#             for e in elements:
#                 if e not in legal_elements:  # 如果elements包含非法字符，就break内部循环，继续外部循环
#                     f.write(id + '\n')
#                     break
#         except Exception as e:
#             print(id, e)
#
# print("***finish process***")

illegal_ligands_path = "data/illegal_ligands_id.txt"
csv_file = "data/all_(0-2]_handcraft.csv"
save_path = "data/all_(0-2]_legal_ligands.csv"

f = open(illegal_ligands_path)
ill_lig = []
for line in f.readlines():
    ill_lig.append(line.strip('\n'))
f.close()

df = pd.read_csv(csv_file)

print("***start process***")
for index, row in df.iterrows():
    id = str(row['ID'])
    ligands = str(row['Unique Ligands'])

    try:
        ligands_list = ligands.split(',')
        ligands_list_new = []
        for l in ligands_list:
            ligands_list_new.append(l.strip())

        if all(l in ill_lig for l in ligands_list_new):
            df.drop(index, inplace=True)

    except Exception as e:
        print(id, e)

df.to_csv(save_path, index=False)
print("***finish process***")
