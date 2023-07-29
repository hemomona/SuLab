# !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
# File       : spy_ligand_info.py
# Time       ：2022/6/3 16:05
# Author     ：Jago
# Email      ：18146856052@163.com
# version    ：python 3.7
# Description：
"""
import random
import time
from socket import timeout
from urllib.error import HTTPError, URLError
from urllib.request import ProxyHandler, build_opener, Request
from bs4 import BeautifulSoup as bs

import pandas as pd

# csv_path = "data/all_(0-2]_handcraft.csv"
# txt_path = "data/all_ligands.txt"
# df = pd.read_csv(csv_path)
# ligands = []
# print("***start process***")
#
# for index, row in df.iterrows():
#     lig_str = str(row['Unique Ligands'])
#     lig_strs = lig_str.split(',')
#
#     for ls in lig_strs:
#         l = ls.strip()
#         if l not in ligands:
#             ligands.append(l)
#
# with open(txt_path, 'a') as f:
#     for l in ligands:
#         f.write(l + "\n")
#
# print("***finish process***")

# txt_path = "data/all_ligands.txt"
# save_path = "data/ligands_img_svg/"
# ligand_url = "https://cdn.rcsb.org/images/ccd/unlabeled/"
# referer_url = "https://www.rcsb.org/"
#
# # 实验室本机IP为125.70.29.65
# proxy = {
#     'http': 'http://49.88.45.181:5021',
#     'https': 'https://49.88.45.181:5021'
# }
# proxy_handler = ProxyHandler(proxy, )
# opener = build_opener(proxy_handler)
# USER_AGENTS_LIST = [
#     "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; AcooBrowser; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
#     "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0; Acoo Browser; SLCC1; .NET CLR 2.0.50727; Media Center PC 5.0; .NET CLR 3.0.04506)",
#     "Mozilla/4.0 (compatible; MSIE 7.0; AOL 9.5; AOLBuild 4337.35; Windows NT 5.1; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
#     "Mozilla/5.0 (Windows; U; MSIE 9.0; Windows NT 9.0; en-US)",
#     "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Win64; x64; Trident/5.0; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 2.0.50727; Media Center PC 6.0)",
#     "Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 1.0.3705; .NET CLR 1.1.4322)",
#     "Mozilla/4.0 (compatible; MSIE 7.0b; Windows NT 5.2; .NET CLR 1.1.4322; .NET CLR 2.0.50727; InfoPath.2; .NET CLR 3.0.04506.30)",
#     "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN) AppleWebKit/523.15 (KHTML, like Gecko, Safari/419.3) Arora/0.3 (Change: 287 c9dfb30)",
#     "Mozilla/5.0 (X11; U; Linux; en-US) AppleWebKit/527+ (KHTML, like Gecko, Safari/419.3) Arora/0.6",
#     "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.2pre) Gecko/20070215 K-Ninja/2.1.1",
#     "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN; rv:1.9) Gecko/20080705 Firefox/3.0 Kapiko/3.0",
#     "Mozilla/5.0 (X11; Linux i686; U;) Gecko/20070322 Kazehakase/0.4.5",
#     "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.8) Gecko Fedora/1.9.0.8-1.fc10 Kazehakase/0.5.6",
#     "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11",
#     "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_3) AppleWebKit/535.20 (KHTML, like Gecko) Chrome/19.0.1036.7 Safari/535.20",
#     "Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; fr) Presto/2.9.168 Version/11.52",
#     "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.11 TaoBrowser/2.0 Safari/536.11",
#     "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.71 Safari/537.1 LBBROWSER",
#     "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E; LBBROWSER)",
#     "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; QQDownload 732; .NET4.0C; .NET4.0E; LBBROWSER)",
#     "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.84 Safari/535.11 LBBROWSER",
#     "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E)",
#     "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E; QQBrowser/7.0.3698.400)",
#     "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; QQDownload 732; .NET4.0C; .NET4.0E)",
#     "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; SV1; QQDownload 732; .NET4.0C; .NET4.0E; 360SE)",
#     "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; QQDownload 732; .NET4.0C; .NET4.0E)",
#     "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E)",
#     "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.89 Safari/537.1",
#     "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.89 Safari/537.1",
#     "Mozilla/5.0 (iPad; U; CPU OS 4_2_1 like Mac OS X; zh-cn) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8C148 Safari/6533.18.5",
#     "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:2.0b13pre) Gecko/20110307 Firefox/4.0b13pre",
#     "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:16.0) Gecko/20100101 Firefox/16.0",
#     "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11",
#     "Mozilla/5.0 (X11; U; Linux x86_64; zh-CN; rv:1.9.2.10) Gecko/20100922 Ubuntu/10.10 (maverick) Firefox/3.6.10"
# ]
# header = {'User-Agent': "",
#           'Referer': referer_url,
#           'sec-ch-ua': "\" Not A;Brand\";v=\"99\", \"Chromium\";v=\"99\", \"Google Chrome\";v=\"99\"",
#           'sec-ch-ua-mobile': "?0",
#           'sec-ch-ua-platform': "Windows",
#           'Sec-Fetch-Dest': "document",
#           'Sec-Fetch-Mode': "navigate",
#           'Sec-Fetch-Site': "same-site",
#           'Sec-Fetch-User': "?1",
#           'Upgrade-Insecure-Requests': "1"
#           }
# print("***start process***")
#
# f = open(txt_path)
# ligands = f.readlines()
# f.close()
#
# lost_ligands = []
# # lost_ligands = ['CA', 'PT']
# for l in ligands:
#     l = l.strip()
#     # if l not in lost_ligands:
#         # continue
#
#     c = l[0]
#     url = ligand_url + c + "/" + l + ".svg"
#     file_name = l + ".svg"
#     file_path = save_path + file_name
#
#     try:
#         header['User-Agent'] = random.choice(USER_AGENTS_LIST)
#         request = Request(url, headers=header)
#         response = opener.open(request, timeout=3)
#
#         print('writing file to', file_path)
#         data = response.read()
#         with open(file_path, "wb") as f:
#             f.write(data)
#     except HTTPError as he:  #
#         lost_ligands.append(l)
#         print("ERROR", url, he)
#     except URLError as ue:  # <urlopen error Tunnel connection failed: 503 Service Unavailable>
#         lost_ligands.append(l)
#         print("ERROR", url, ue)
#     except timeout as te:  # socket.timeout: The read operation timed out
#         lost_ligands.append(l)
#         print("ERROR", url, te)
#
#     time.sleep(random.random() * 3)  # 担心被封
#
# print("***finish process***")
# print(lost_ligands)

txt_path = "data/all_ligands.txt"
csv_path = "data/all_ligands.csv"
ligand_url = "https://www.rcsb.org/ligand/"

# 实验室本机IP为125.70.29.65
proxy = {
    'http': 'http://49.88.45.181:5021',
    'https': 'https://49.88.45.181:5021'
}
proxy_handler = ProxyHandler(proxy, )
opener = build_opener(proxy_handler)
USER_AGENTS_LIST = [
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; AcooBrowser; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0; Acoo Browser; SLCC1; .NET CLR 2.0.50727; Media Center PC 5.0; .NET CLR 3.0.04506)",
    "Mozilla/4.0 (compatible; MSIE 7.0; AOL 9.5; AOLBuild 4337.35; Windows NT 5.1; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
    "Mozilla/5.0 (Windows; U; MSIE 9.0; Windows NT 9.0; en-US)",
    "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Win64; x64; Trident/5.0; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 2.0.50727; Media Center PC 6.0)",
    "Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 1.0.3705; .NET CLR 1.1.4322)",
    "Mozilla/4.0 (compatible; MSIE 7.0b; Windows NT 5.2; .NET CLR 1.1.4322; .NET CLR 2.0.50727; InfoPath.2; .NET CLR 3.0.04506.30)",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN) AppleWebKit/523.15 (KHTML, like Gecko, Safari/419.3) Arora/0.3 (Change: 287 c9dfb30)",
    "Mozilla/5.0 (X11; U; Linux; en-US) AppleWebKit/527+ (KHTML, like Gecko, Safari/419.3) Arora/0.6",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.2pre) Gecko/20070215 K-Ninja/2.1.1",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN; rv:1.9) Gecko/20080705 Firefox/3.0 Kapiko/3.0",
    "Mozilla/5.0 (X11; Linux i686; U;) Gecko/20070322 Kazehakase/0.4.5",
    "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.8) Gecko Fedora/1.9.0.8-1.fc10 Kazehakase/0.5.6",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_3) AppleWebKit/535.20 (KHTML, like Gecko) Chrome/19.0.1036.7 Safari/535.20",
    "Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; fr) Presto/2.9.168 Version/11.52",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.11 TaoBrowser/2.0 Safari/536.11",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.71 Safari/537.1 LBBROWSER",
    "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E; LBBROWSER)",
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; QQDownload 732; .NET4.0C; .NET4.0E; LBBROWSER)",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.84 Safari/535.11 LBBROWSER",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E)",
    "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E; QQBrowser/7.0.3698.400)",
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; QQDownload 732; .NET4.0C; .NET4.0E)",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; SV1; QQDownload 732; .NET4.0C; .NET4.0E; 360SE)",
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; QQDownload 732; .NET4.0C; .NET4.0E)",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E)",
    "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.89 Safari/537.1",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.89 Safari/537.1",
    "Mozilla/5.0 (iPad; U; CPU OS 4_2_1 like Mac OS X; zh-cn) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8C148 Safari/6533.18.5",
    "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:2.0b13pre) Gecko/20110307 Firefox/4.0b13pre",
    "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:16.0) Gecko/20100101 Firefox/16.0",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11",
    "Mozilla/5.0 (X11; U; Linux x86_64; zh-CN; rv:1.9.2.10) Gecko/20100922 Ubuntu/10.10 (maverick) Firefox/3.6.10"
]
header = {'User-Agent': "",
          'Cache-Control': "max-age=0",
          'sec-ch-ua': "\" Not A;Brand\";v=\"99\", \"Chromium\";v=\"99\", \"Google Chrome\";v=\"99\"",
          'sec-ch-ua-mobile': "?0",
          'sec-ch-ua-platform': "Windows",
          'Sec-Fetch-Dest': "document",
          'Sec-Fetch-Mode': "navigate",
          'Sec-Fetch-Site': "same-site",
          'Sec-Fetch-User': "?1",
          'Upgrade-Insecure-Requests': "1"
          }
print("***start process***")

ligands = []
f = open(txt_path)
while True:
    line = f.readline()
    if not line:
        break
    ligands.append(line.strip())
f.close()

# lost_ligands = []
lost_ligands = ['G2F', 'DPM', 'TB', 'CE2', 'NAT', 'SFC', 'MVD', 'ZIO', 'COS', '983', 'SR1', 'YM7', 'SYD', 'D7A', 'X2X', 'N6T', '3U2', '8VT']

table_format = {"ID": [], "Name": [], "Identifiers": [], "Formula": [], "Molecular Weight": [],
                "Type": [], "Isomeric SMILES": [], "InChI": [], "InChIKey": [], "Formal Charge": [],
                "Atom Count": [], "Chiral Atom Count": [], "Bond Count": [], "Aromatic Bond Count": []}

i = 0
for l in ligands:
    if l not in lost_ligands:
        continue

    url = ligand_url + l
    print("accessing", url)

    try:
        header['User-Agent'] = random.choice(USER_AGENTS_LIST)
        request = Request(url, headers=header)
        response = opener.open(request, timeout=10)
        response = response.read().decode('utf-8')
        obj = bs(response, 'html.parser')

        name = obj.find('tr', id="chemicalName").td.get_text() if obj.find('tr', id="chemicalName") else ""
        ide = obj.find("tr", id="chemicalIdentifiers").td.get_text() if obj.find("tr", id="chemicalIdentifiers") else ""
        formula = obj.find('tr', id="chemicalFormula").td.get_text() if obj.find('tr', id="chemicalFormula") else ""
        weight = obj.find('tr', id="chemicalMolecularWeight").td.get_text() if obj.find('tr', id="chemicalMolecularWeight") else ""
        typ = obj.find('tr', id="chemicalType").td.get_text() if obj.find('tr', id="chemicalType") else ""
        iso = obj.find('tr', id="chemicalIsomeric").td.get_text() if obj.find('tr', id="chemicalIsomeric") else ""
        ici = obj.find('tr', id="chemicalInChI").td.get_text() if obj.find('tr', id="chemicalInChI") else ""
        icikey = obj.find('tr', id="chemicalInChIKey").td.get_text() if obj.find('tr', id="chemicalInChIKey") else ""
        fc = obj.find('tr', id="chemicalFormalCharge").td.get_text() if obj.find('tr', id="chemicalFormalCharge") else ""
        ac = obj.find('tr', id="chemicalAtomCount").td.get_text() if obj.find('tr', id="chemicalAtomCount") else ""
        cac = obj.find('tr', id="chemicalChiralAtomCount").td.get_text() if obj.find('tr', id="chemicalChiralAtomCount") else ""
        bc = obj.find('tr', id="chemicalBondCount").td.get_text() if obj.find('tr', id="chemicalBondCount") else ""
        aac = obj.find('tr', id="chemicalAromaticAtomCount").td.get_text() if obj.find('tr', id="chemicalAromaticAtomCount") else ""

        # 提取数据
        table_format['ID'].append(l)
        table_format['Name'].append(name)
        table_format['Identifiers'].append(ide)  # 可能有记录不存在该项
        table_format['Formula'].append(formula)
        table_format['Molecular Weight'].append(weight)
        table_format['Type'].append(typ)
        table_format['Isomeric SMILES'].append(iso)
        table_format['InChI'].append(ici)
        table_format['InChIKey'].append(icikey)
        table_format['Formal Charge'].append(fc)
        table_format['Atom Count'].append(ac)
        table_format['Chiral Atom Count'].append(cac)
        table_format['Bond Count'].append(bc)
        table_format['Aromatic Bond Count'].append(aac)

        i += 1

        if i == 50:
            i = 0
            table_copy = table_format.copy()
            table_format = {"ID": [], "Name": [], "Identifiers": [], "Formula": [], "Molecular Weight": [],
                            "Type": [], "Isomeric SMILES": [], "InChI": [], "InChIKey": [], "Formal Charge": [],
                            "Atom Count": [], "Chiral Atom Count": [], "Bond Count": [], "Aromatic Bond Count": []}
            # 下一行！！！报错All arrays must be of the same length，代表前50行都没有录入！！！
            # 这种情况，后续步骤都不会执行，即不会重置i与table_format，会继续循环，但不会进入该判断并写入文件
            # 因此将重置函数置于最前，避免一段出错，全部不写
            df = pd.DataFrame(data=table_copy)
            df[['ID']] = df[['ID']].astype(str)
            df.to_csv(csv_path, header=False, index=False, mode='a')
            # 重置i与table_format
            # i = 0
            # table_format = {"ID": [], "Name": [], "Identifiers": [], "Formula": [], "Molecular Weight": [],
            #                 "Type": [], "Isomeric SMILES": [], "InChI": [], "InChIKey": [], "Formal Charge": [],
            #                 "Atom Count": [], "Chiral Atom Count": [], "Bond Count": [], "Aromatic Bond Count": []}
            print("+ 50 rows")

    except Exception as e:
        lost_ligands.append(l)
        print("ERROR", l, e)

    time.sleep(random.random())  # 担心被封

# 最后一次不足50条的数据加入
df = pd.DataFrame(data=table_format)
df[['ID']] = df[['ID']].astype(str)
df.to_csv(csv_path, header=False, index=False, mode='a')

print("***finish process***")
print(lost_ligands)
