# !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
# File       : spy_pdb_file.py
# Time       ：2022/6/1 11:05
# Author     ：Jago
# Email      ：18146856052@163.com
# version    ：python 3.7
# Description：
"""
import time

import pandas as pd
import requests
from urllib.request import build_opener, ProxyHandler, Request

xlsx_path = "data/RNA_0-2_raw.xlsx"
save_path = "data/rna/"
pdb_url = "https://files.rcsb.org/download/"

df = pd.read_excel(xlsx_path, index_col=0)
# print(df.loc['5MEH'])
# print(df.loc[['5MEH', '1LKK']])
# print(df.loc[:, 'pro'])
IDs = df.index.tolist()

# header = {
#         'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.64 Safari/537.36 Edg/101.0.1210.53',
#         'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
#         'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6'}
proxy = {
    'http': 'http://49.88.45.181:5021',
    'https': 'https://49.88.45.181:5021'
}
proxy_handler = ProxyHandler(proxy, )
opener = build_opener(proxy_handler)

print("***start process***")

for id in IDs:
    if not isinstance(id, str):
        print("***skip*** ", str(id))
        continue
    url = pdb_url + id + ".pdb"
    resolution = round(df.at[id, 'Resolution'], 2)
    ligands = df.at[id, 'Unique Ligands']
    file_name = id + "_rna_" + str(resolution) + "A_" + ligands + ".pdb"
    file_path = save_path + file_name

    # url = "http://httpbin.org/get"
    # t = requests.get(url, headers=header, proxies=proxy)
    # print(t.json()["origin"])
    request = Request(url)
    response = opener.open(request)
    # response = requests.get(url, headers=header, proxies=proxy)

    print('writing file: ', id)
    data = response.read()
    with open(file_path, "wb") as f:
        f.write(data)

    time.sleep(5)  # 担心被封

print("***finish process***")
