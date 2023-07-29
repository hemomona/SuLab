# !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
# File       : spy_test1.py
# Time       ：2022/5/30 16:13
# Author     ：Jago
# Email      ：18146856052@163.com
# version    ：python 3.7
# Description：
"""
# 安装bs4命令: pip3 install beautifulsoup4 -i http://pypi.douban.com/simple --trusted-host pypi.douban.com
# rcsb网址在https://kmcha.com/text-compare对比找出规律: start%22%3A0%7D%2C%22 更改3A之后的值0，100，200...

# 导入urllib库的urlopen函数
from urllib.request import urlopen
# 导入BeautifulSoup
import requests as requests
from requests.adapters import HTTPAdapter
from requests.packages.urllib3.util.retry import Retry
from bs4 import BeautifulSoup as bs

url = "https://www.rcsb.org/search?request=%7B%22query%22%3A%7B%22type%22%3A%22group%22%2C%22logical_operator%22%3A%22and%22%2C%22nodes%22%3A%5B%7B%22type%22%3A%22group%22%2C%22logical_operator%22%3A%22and%22%2C%22nodes%22%3A%5B%7B%22type%22%3A%22group%22%2C%22nodes%22%3A%5B%7B%22type%22%3A%22group%22%2C%22nodes%22%3A%5B%7B%22type%22%3A%22terminal%22%2C%22service%22%3A%22text%22%2C%22parameters%22%3A%7B%22attribute%22%3A%22entity_poly.rcsb_entity_polymer_type%22%2C%22value%22%3A%22Protein%22%2C%22operator%22%3A%22exact_match%22%7D%7D%5D%2C%22logical_operator%22%3A%22or%22%2C%22label%22%3A%22entity_poly.rcsb_entity_polymer_type%22%7D%2C%7B%22type%22%3A%22group%22%2C%22nodes%22%3A%5B%7B%22type%22%3A%22terminal%22%2C%22service%22%3A%22text%22%2C%22parameters%22%3A%7B%22attribute%22%3A%22rcsb_entry_info.resolution_combined%22%2C%22value%22%3A0.5%2C%22operator%22%3A%22less%22%7D%7D%2C%7B%22type%22%3A%22terminal%22%2C%22service%22%3A%22text%22%2C%22parameters%22%3A%7B%22attribute%22%3A%22rcsb_entry_info.resolution_combined%22%2C%22value%22%3A%7B%22from%22%3A0.5%2C%22to%22%3A1%2C%22include_lower%22%3Atrue%2C%22include_upper%22%3Atrue%7D%2C%22operator%22%3A%22range%22%7D%7D%5D%2C%22logical_operator%22%3A%22or%22%2C%22label%22%3A%22rcsb_entry_info.resolution_combined%22%7D%5D%2C%22logical_operator%22%3A%22and%22%7D%5D%2C%22label%22%3A%22text%22%7D%5D%7D%2C%22return_type%22%3A%22entry%22%2C%22request_options%22%3A%7B%22paginate%22%3A%7B%22rows%22%3A100%2C%22start%22%3A0%7D%2C%22scoring_strategy%22%3A%22combined%22%2C%22sort%22%3A%5B%7B%22sort_by%22%3A%22score%22%2C%22direction%22%3A%22desc%22%7D%5D%7D%2C%22request_info%22%3A%7B%22query_id%22%3A%2233c7c85d28122c7a00fd87be4aa802d2%22%7D%7D"
header = {'user-agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:45.0) Gecko/20100101 Firefox/45.0', 'Connection': 'close'}
session = requests.Session()
retry = Retry(connect=3, backoff_factor=0.5)
adapter = HTTPAdapter(max_retries=retry)
session.mount('http://', adapter)
session.mount('https://', adapter)
# 请求获取html
# html = urlopen(url)
# html = urlopen("http://www.baidu.com")

response = session.get(url, headers=header)
response.encoding = response.apparent_encoding
# 用BeautifulSoup解析html
# obj = bs(html.read(), 'html.parser')
obj = bs(response.content, 'html.parser')
# 提取results-item
results_item = obj.find_all('div', class_="results-item")
print(obj)
# # 提取logo图片的链接
# logo_url = "https:"+logo_pic_info[0]['src']
# # 使用urlretrieve下载图片
# urlretrieve(logo_url, 'data/logo.png')

