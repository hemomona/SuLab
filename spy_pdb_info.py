# !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
# File       : spy_pdb_info.py
# Time       ：2022/5/31 8:56
# Author     ：Jago
# Email      ：18146856052@163.com
# version    ：python 3.7
# Description：chrome version: 99.0.4844.51
               参考https://www.cnblogs.com/lfri/p/10542797.html安装selenium package与chrome driver
"""
import time
from selenium import webdriver
from selenium.common import WebDriverException, TimeoutException
from selenium.webdriver.common.by import By

import pandas as pd

chrome_option = webdriver.ChromeOptions()
chrome_option.add_argument('--headless')  # 设置后台运行，不显示浏览器
chrome_option.add_argument("--proxy-server=49.88.45.181:5021")  # 设置代理
webdriver.DesiredCapabilities.CHROME['acceptSslCerts'] = True
browser = webdriver.Chrome(options=chrome_option)

# browser.implicitly_wait(10)  # 隐式等待 10s
# 下面是(0, 1]的pro网址 13页 1202
# init_url = "https://www.rcsb.org/search?request=%7B%22query%22%3A%7B%22type%22%3A%22group%22%2C%22logical_operator%22%3A%22and%22%2C%22nodes%22%3A%5B%7B%22type%22%3A%22group%22%2C%22logical_operator%22%3A%22and%22%2C%22nodes%22%3A%5B%7B%22type%22%3A%22group%22%2C%22nodes%22%3A%5B%7B%22type%22%3A%22group%22%2C%22nodes%22%3A%5B%7B%22type%22%3A%22terminal%22%2C%22service%22%3A%22text%22%2C%22parameters%22%3A%7B%22attribute%22%3A%22entity_poly.rcsb_entity_polymer_type%22%2C%22value%22%3A%22Protein%22%2C%22operator%22%3A%22exact_match%22%7D%7D%5D%2C%22logical_operator%22%3A%22or%22%2C%22label%22%3A%22entity_poly.rcsb_entity_polymer_type%22%7D%2C%7B%22type%22%3A%22group%22%2C%22nodes%22%3A%5B%7B%22type%22%3A%22terminal%22%2C%22service%22%3A%22text%22%2C%22parameters%22%3A%7B%22attribute%22%3A%22rcsb_entry_info.resolution_combined%22%2C%22value%22%3A0.5%2C%22operator%22%3A%22less%22%7D%7D%2C%7B%22type%22%3A%22terminal%22%2C%22service%22%3A%22text%22%2C%22parameters%22%3A%7B%22attribute%22%3A%22rcsb_entry_info.resolution_combined%22%2C%22value%22%3A%7B%22from%22%3A0.5%2C%22to%22%3A1%2C%22include_lower%22%3Atrue%2C%22include_upper%22%3Atrue%7D%2C%22operator%22%3A%22range%22%7D%7D%5D%2C%22logical_operator%22%3A%22or%22%2C%22label%22%3A%22rcsb_entry_info.resolution_combined%22%7D%5D%2C%22logical_operator%22%3A%22and%22%7D%5D%2C%22label%22%3A%22text%22%7D%5D%7D%2C%22return_type%22%3A%22entry%22%2C%22request_options%22%3A%7B%22paginate%22%3A%7B%22rows%22%3A100%2C%22start%22%3A0%7D%2C%22scoring_strategy%22%3A%22combined%22%2C%22sort%22%3A%5B%7B%22sort_by%22%3A%22score%22%2C%22direction%22%3A%22desc%22%7D%5D%7D%2C%22request_info%22%3A%7B%22query_id%22%3A%2233c7c85d28122c7a00fd87be4aa802d2%22%7D%7D"
# 下面是[1, 2]的pro网址 798页 79800
# init_url = "https://www.rcsb.org/search?request=%7B%22query%22%3A%7B%22type%22%3A%22group%22%2C%22logical_operator%22%3A%22and%22%2C%22nodes%22%3A%5B%7B%22type%22%3A%22group%22%2C%22logical_operator%22%3A%22and%22%2C%22nodes%22%3A%5B%7B%22type%22%3A%22group%22%2C%22nodes%22%3A%5B%7B%22type%22%3A%22group%22%2C%22nodes%22%3A%5B%7B%22type%22%3A%22terminal%22%2C%22service%22%3A%22text%22%2C%22parameters%22%3A%7B%22attribute%22%3A%22entity_poly.rcsb_entity_polymer_type%22%2C%22value%22%3A%22Protein%22%2C%22operator%22%3A%22exact_match%22%7D%7D%5D%2C%22logical_operator%22%3A%22or%22%2C%22label%22%3A%22entity_poly.rcsb_entity_polymer_type%22%7D%2C%7B%22type%22%3A%22group%22%2C%22nodes%22%3A%5B%7B%22type%22%3A%22terminal%22%2C%22service%22%3A%22text%22%2C%22parameters%22%3A%7B%22attribute%22%3A%22rcsb_entry_info.resolution_combined%22%2C%22value%22%3A%7B%22from%22%3A1%2C%22to%22%3A2%2C%22include_lower%22%3Atrue%2C%22include_upper%22%3Atrue%7D%2C%22operator%22%3A%22range%22%7D%7D%5D%2C%22logical_operator%22%3A%22or%22%2C%22label%22%3A%22rcsb_entry_info.resolution_combined%22%7D%5D%2C%22logical_operator%22%3A%22and%22%7D%5D%2C%22label%22%3A%22text%22%7D%5D%7D%2C%22return_type%22%3A%22entry%22%2C%22request_options%22%3A%7B%22paginate%22%3A%7B%22rows%22%3A100%2C%22start%22%3A0%7D%2C%22scoring_strategy%22%3A%22combined%22%2C%22sort%22%3A%5B%7B%22sort_by%22%3A%22score%22%2C%22direction%22%3A%22desc%22%7D%5D%7D%2C%22request_info%22%3A%7B%22query_id%22%3A%222b2688db797a2c1ac8c9bb4cd3acbe66%22%7D%7D"
# 下面是(0, 2]的rna网址 8页 773
# init_url = "https://www.rcsb.org/search?request=%7B%22query%22%3A%7B%22type%22%3A%22group%22%2C%22logical_operator%22%3A%22and%22%2C%22nodes%22%3A%5B%7B%22type%22%3A%22group%22%2C%22logical_operator%22%3A%22and%22%2C%22nodes%22%3A%5B%7B%22type%22%3A%22group%22%2C%22nodes%22%3A%5B%7B%22type%22%3A%22group%22%2C%22nodes%22%3A%5B%7B%22type%22%3A%22terminal%22%2C%22service%22%3A%22text%22%2C%22parameters%22%3A%7B%22attribute%22%3A%22entity_poly.rcsb_entity_polymer_type%22%2C%22value%22%3A%22RNA%22%2C%22operator%22%3A%22exact_match%22%7D%7D%5D%2C%22logical_operator%22%3A%22or%22%2C%22label%22%3A%22entity_poly.rcsb_entity_polymer_type%22%7D%2C%7B%22type%22%3A%22group%22%2C%22nodes%22%3A%5B%7B%22type%22%3A%22terminal%22%2C%22service%22%3A%22text%22%2C%22parameters%22%3A%7B%22attribute%22%3A%22rcsb_entry_info.resolution_combined%22%2C%22value%22%3A%7B%22from%22%3A1%2C%22to%22%3A2%2C%22include_lower%22%3Atrue%2C%22include_upper%22%3Atrue%7D%2C%22operator%22%3A%22range%22%2C%22negation%22%3Afalse%7D%7D%2C%7B%22type%22%3A%22terminal%22%2C%22service%22%3A%22text%22%2C%22parameters%22%3A%7B%22attribute%22%3A%22rcsb_entry_info.resolution_combined%22%2C%22operator%22%3A%22less%22%2C%22negation%22%3Afalse%2C%22value%22%3A1%7D%7D%5D%2C%22logical_operator%22%3A%22or%22%2C%22label%22%3A%22rcsb_entry_info.resolution_combined%22%7D%5D%2C%22logical_operator%22%3A%22and%22%7D%5D%2C%22label%22%3A%22text%22%7D%5D%7D%2C%22return_type%22%3A%22entry%22%2C%22request_options%22%3A%7B%22paginate%22%3A%7B%22rows%22%3A100%2C%22start%22%3A0%7D%2C%22scoring_strategy%22%3A%22combined%22%2C%22sort%22%3A%5B%7B%22sort_by%22%3A%22score%22%2C%22direction%22%3A%22desc%22%7D%5D%7D%2C%22request_info%22%3A%7B%22query_id%22%3A%22c782abf40f6e8e862600a43a25aac468%22%7D%7D"
# 下面是(0, 2]的dna网址 23页 2294
# init_url = "https://www.rcsb.org/search?request=%7B%22query%22%3A%7B%22type%22%3A%22group%22%2C%22logical_operator%22%3A%22and%22%2C%22nodes%22%3A%5B%7B%22type%22%3A%22group%22%2C%22logical_operator%22%3A%22and%22%2C%22nodes%22%3A%5B%7B%22type%22%3A%22group%22%2C%22nodes%22%3A%5B%7B%22type%22%3A%22group%22%2C%22nodes%22%3A%5B%7B%22type%22%3A%22terminal%22%2C%22service%22%3A%22text%22%2C%22parameters%22%3A%7B%22attribute%22%3A%22entity_poly.rcsb_entity_polymer_type%22%2C%22value%22%3A%22DNA%22%2C%22operator%22%3A%22exact_match%22%7D%7D%5D%2C%22logical_operator%22%3A%22or%22%2C%22label%22%3A%22entity_poly.rcsb_entity_polymer_type%22%7D%2C%7B%22type%22%3A%22group%22%2C%22nodes%22%3A%5B%7B%22type%22%3A%22terminal%22%2C%22service%22%3A%22text%22%2C%22parameters%22%3A%7B%22attribute%22%3A%22rcsb_entry_info.resolution_combined%22%2C%22value%22%3A%7B%22from%22%3A1%2C%22to%22%3A2%2C%22include_lower%22%3Atrue%2C%22include_upper%22%3Atrue%7D%2C%22operator%22%3A%22range%22%2C%22negation%22%3Afalse%7D%7D%2C%7B%22type%22%3A%22terminal%22%2C%22service%22%3A%22text%22%2C%22parameters%22%3A%7B%22attribute%22%3A%22rcsb_entry_info.resolution_combined%22%2C%22operator%22%3A%22less%22%2C%22negation%22%3Afalse%2C%22value%22%3A1%7D%7D%5D%2C%22logical_operator%22%3A%22or%22%2C%22label%22%3A%22rcsb_entry_info.resolution_combined%22%7D%5D%2C%22logical_operator%22%3A%22and%22%7D%5D%2C%22label%22%3A%22text%22%7D%5D%7D%2C%22return_type%22%3A%22entry%22%2C%22request_options%22%3A%7B%22paginate%22%3A%7B%22rows%22%3A100%2C%22start%22%3A0%7D%2C%22scoring_strategy%22%3A%22combined%22%2C%22sort%22%3A%5B%7B%22sort_by%22%3A%22score%22%2C%22direction%22%3A%22desc%22%7D%5D%7D%2C%22request_info%22%3A%7B%22query_id%22%3A%225bd8b3e0edc0ce236b51940692f5bbda%22%7D%7D"
# 下面是(0, 2]的pro/na网址 18页 1789
# init_url = "https://www.rcsb.org/search?request=%7B%22query%22%3A%7B%22type%22%3A%22group%22%2C%22logical_operator%22%3A%22and%22%2C%22nodes%22%3A%5B%7B%22type%22%3A%22group%22%2C%22logical_operator%22%3A%22and%22%2C%22nodes%22%3A%5B%7B%22type%22%3A%22group%22%2C%22nodes%22%3A%5B%7B%22type%22%3A%22group%22%2C%22nodes%22%3A%5B%7B%22type%22%3A%22terminal%22%2C%22service%22%3A%22text%22%2C%22parameters%22%3A%7B%22attribute%22%3A%22rcsb_entry_info.selected_polymer_entity_types%22%2C%22operator%22%3A%22exact_match%22%2C%22negation%22%3Afalse%2C%22value%22%3A%22Protein%2FNA%22%7D%7D%5D%2C%22logical_operator%22%3A%22or%22%2C%22label%22%3A%22entity_poly.rcsb_entity_polymer_type%22%7D%2C%7B%22type%22%3A%22group%22%2C%22nodes%22%3A%5B%7B%22type%22%3A%22terminal%22%2C%22service%22%3A%22text%22%2C%22parameters%22%3A%7B%22attribute%22%3A%22rcsb_entry_info.resolution_combined%22%2C%22value%22%3A%7B%22from%22%3A1%2C%22to%22%3A2%2C%22include_lower%22%3Atrue%2C%22include_upper%22%3Atrue%7D%2C%22operator%22%3A%22range%22%2C%22negation%22%3Afalse%7D%7D%2C%7B%22type%22%3A%22terminal%22%2C%22service%22%3A%22text%22%2C%22parameters%22%3A%7B%22attribute%22%3A%22rcsb_entry_info.resolution_combined%22%2C%22operator%22%3A%22less%22%2C%22negation%22%3Afalse%2C%22value%22%3A1%7D%7D%5D%2C%22logical_operator%22%3A%22or%22%2C%22label%22%3A%22rcsb_entry_info.resolution_combined%22%7D%5D%2C%22logical_operator%22%3A%22and%22%7D%5D%2C%22label%22%3A%22text%22%7D%5D%7D%2C%22return_type%22%3A%22entry%22%2C%22request_options%22%3A%7B%22paginate%22%3A%7B%22rows%22%3A100%2C%22start%22%3A0%7D%2C%22scoring_strategy%22%3A%22combined%22%2C%22sort%22%3A%5B%7B%22sort_by%22%3A%22score%22%2C%22direction%22%3A%22desc%22%7D%5D%7D%2C%22request_info%22%3A%7B%22query_id%22%3A%22be072291831a34498c808f1af8d00cba%22%7D%7D"
# 下面是(0, 2]的na(only)网址 12页 1160
# init_url = "https://www.rcsb.org/search?request=%7B%22query%22%3A%7B%22type%22%3A%22group%22%2C%22logical_operator%22%3A%22and%22%2C%22nodes%22%3A%5B%7B%22type%22%3A%22group%22%2C%22logical_operator%22%3A%22and%22%2C%22nodes%22%3A%5B%7B%22type%22%3A%22group%22%2C%22nodes%22%3A%5B%7B%22type%22%3A%22group%22%2C%22nodes%22%3A%5B%7B%22type%22%3A%22terminal%22%2C%22service%22%3A%22text%22%2C%22parameters%22%3A%7B%22attribute%22%3A%22rcsb_entry_info.selected_polymer_entity_types%22%2C%22operator%22%3A%22exact_match%22%2C%22negation%22%3Afalse%2C%22value%22%3A%22Nucleic%20acid%20(only)%22%7D%7D%5D%2C%22logical_operator%22%3A%22or%22%2C%22label%22%3A%22entity_poly.rcsb_entity_polymer_type%22%7D%2C%7B%22type%22%3A%22group%22%2C%22nodes%22%3A%5B%7B%22type%22%3A%22terminal%22%2C%22service%22%3A%22text%22%2C%22parameters%22%3A%7B%22attribute%22%3A%22rcsb_entry_info.resolution_combined%22%2C%22value%22%3A%7B%22from%22%3A1%2C%22to%22%3A2%2C%22include_lower%22%3Atrue%2C%22include_upper%22%3Atrue%7D%2C%22operator%22%3A%22range%22%2C%22negation%22%3Afalse%7D%7D%2C%7B%22type%22%3A%22terminal%22%2C%22service%22%3A%22text%22%2C%22parameters%22%3A%7B%22attribute%22%3A%22rcsb_entry_info.resolution_combined%22%2C%22operator%22%3A%22less%22%2C%22negation%22%3Afalse%2C%22value%22%3A1%7D%7D%5D%2C%22logical_operator%22%3A%22or%22%2C%22label%22%3A%22rcsb_entry_info.resolution_combined%22%7D%5D%2C%22logical_operator%22%3A%22and%22%7D%5D%2C%22label%22%3A%22text%22%7D%5D%7D%2C%22return_type%22%3A%22entry%22%2C%22request_options%22%3A%7B%22paginate%22%3A%7B%22rows%22%3A100%2C%22start%22%3A0%7D%2C%22scoring_strategy%22%3A%22combined%22%2C%22sort%22%3A%5B%7B%22sort_by%22%3A%22score%22%2C%22direction%22%3A%22desc%22%7D%5D%7D%2C%22request_info%22%3A%7B%22query_id%22%3A%22b899cc21d734dbff883d424e09e83fe2%22%7D%7D"
# 下面是(0, 2]的pro(only)网址 754页 75325
# init_url = "https://www.rcsb.org/search?request=%7B%22query%22%3A%7B%22type%22%3A%22group%22%2C%22logical_operator%22%3A%22and%22%2C%22nodes%22%3A%5B%7B%22type%22%3A%22group%22%2C%22logical_operator%22%3A%22and%22%2C%22nodes%22%3A%5B%7B%22type%22%3A%22group%22%2C%22nodes%22%3A%5B%7B%22type%22%3A%22group%22%2C%22nodes%22%3A%5B%7B%22type%22%3A%22terminal%22%2C%22service%22%3A%22text%22%2C%22parameters%22%3A%7B%22attribute%22%3A%22rcsb_entry_info.selected_polymer_entity_types%22%2C%22operator%22%3A%22exact_match%22%2C%22negation%22%3Afalse%2C%22value%22%3A%22Protein%20(only)%22%7D%7D%5D%2C%22logical_operator%22%3A%22or%22%2C%22label%22%3A%22entity_poly.rcsb_entity_polymer_type%22%7D%2C%7B%22type%22%3A%22group%22%2C%22nodes%22%3A%5B%7B%22type%22%3A%22terminal%22%2C%22service%22%3A%22text%22%2C%22parameters%22%3A%7B%22attribute%22%3A%22rcsb_entry_info.resolution_combined%22%2C%22value%22%3A%7B%22from%22%3A1%2C%22to%22%3A2%2C%22include_lower%22%3Atrue%2C%22include_upper%22%3Atrue%7D%2C%22operator%22%3A%22range%22%2C%22negation%22%3Afalse%7D%7D%2C%7B%22type%22%3A%22terminal%22%2C%22service%22%3A%22text%22%2C%22parameters%22%3A%7B%22attribute%22%3A%22rcsb_entry_info.resolution_combined%22%2C%22operator%22%3A%22less%22%2C%22negation%22%3Afalse%2C%22value%22%3A1%7D%7D%5D%2C%22logical_operator%22%3A%22or%22%2C%22label%22%3A%22rcsb_entry_info.resolution_combined%22%7D%5D%2C%22logical_operator%22%3A%22and%22%7D%5D%2C%22label%22%3A%22text%22%7D%5D%7D%2C%22return_type%22%3A%22entry%22%2C%22request_options%22%3A%7B%22paginate%22%3A%7B%22rows%22%3A100%2C%22start%22%3A0%7D%2C%22scoring_strategy%22%3A%22combined%22%2C%22sort%22%3A%5B%7B%22sort_by%22%3A%22score%22%2C%22direction%22%3A%22desc%22%7D%5D%7D%2C%22request_info%22%3A%7B%22query_id%22%3A%22a7b9e014c16f6a0c4c0012a389c5ed6c%22%7D%7D"
# 下面是(0, 2]的pdb网址 820页 81989
init_url = "https://www.rcsb.org/search?request=%7B%22query%22%3A%7B%22type%22%3A%22group%22%2C%22logical_operator%22%3A%22and%22%2C%22nodes%22%3A%5B%7B%22type%22%3A%22group%22%2C%22logical_operator%22%3A%22and%22%2C%22nodes%22%3A%5B%7B%22type%22%3A%22group%22%2C%22nodes%22%3A%5B%7B%22type%22%3A%22terminal%22%2C%22service%22%3A%22text%22%2C%22parameters%22%3A%7B%22attribute%22%3A%22rcsb_entry_info.resolution_combined%22%2C%22operator%22%3A%22less_or_equal%22%2C%22negation%22%3Afalse%2C%22value%22%3A2%7D%7D%5D%2C%22logical_operator%22%3A%22and%22%7D%5D%2C%22label%22%3A%22text%22%7D%5D%7D%2C%22return_type%22%3A%22entry%22%2C%22request_options%22%3A%7B%22paginate%22%3A%7B%22rows%22%3A100%2C%22start%22%3A0%7D%2C%22scoring_strategy%22%3A%22combined%22%2C%22sort%22%3A%5B%7B%22sort_by%22%3A%22score%22%2C%22direction%22%3A%22desc%22%7D%5D%7D%2C%22request_info%22%3A%7B%22query_id%22%3A%22a809beaa359fa969da69fb20ba74f563%22%7D%7D"
save_path = "data/all_(0-2]_raw.csv"
# url = "file://D:/code/SuLab/data/RCSB_test.html"
total_page = 820
urls = []
urls.append(init_url)
p = 1
while p < total_page:
    urls.append(init_url.replace("start%22%3A", "start%22%3A"+str(p)+str(0)))
    p += 1
print("***start process***")

# results = WebDriverWait(browser, 10).until(
#     expected_conditions.presence_of_element_located((By.XPATH, "//div[@class='results-item']/..")))
# 直接查询row results-item-row返回NULL
# results_items = browser.find_elements(by=By.CLASS_NAME, value='row results-item-row')
# 直接查询results-item可以返回列表，看来不能直接使用嵌套内部的class name查询
# results_items = browser.find_elements(by=By.CLASS_NAME, value='results-item')

# 存储上一轮未能成功爬取的页面
# lost_page = []
lost_page = [33, 696, 735, 813]

page = 0
while page < total_page:
    # 如果初始lost_page设为[]，注释下三行即可
    if page not in lost_page:
        page += 1
        continue

    try:
        browser.get(urls[page])
        time.sleep(10)
        # html中的img链接列表，从中提取PDB ID
        results_item_imgs = browser.find_elements(by=By.XPATH, value="//div[@class='results-item']"
                                                                     "/div[@class='row results-item-row']"
                                                                     "/div[@class='col-md-3 col-xs-12 results-item-img']"
                                                                     "/a")
        # html中的蛋白信息列表，从中提取info_dict后6项
        results_item_infos = browser.find_elements(by=By.XPATH, value="//div[@class='results-item']"
                                                                      "/div[@class='row results-item-row']"
                                                                      "/div[@class='col-md-9 col-xs-12 results-item-info']"
                                                                      "/table[@class='results-item-data']")

        info_list = []
        # 直接归类到info_dict
        i = 0
        for i in range(len(results_item_imgs)):
            # info_dict中的method包含了table_format中的Method和Resolution两项
            info_dict = {"ID": "", "href": "", "Released": "", "Method": "", "Organisms": "",
                         "Macromolecule": "", "Unique Ligands": "", "Unique branched monosaccharides": ""}
            img = results_item_imgs[i]
            info = results_item_infos[i]
            labels = info.find_elements(by=By.CSS_SELECTOR, value='table td:nth-of-type(odd)')
            values = info.find_elements(by=By.CSS_SELECTOR, value='table td:nth-of-type(even)')

            info_dict["ID"] = img.get_attribute('href')[-4:]
            info_dict["href"] = img.get_attribute('href')
            j = 0  # 每个蛋白的信息条目在4~6条之间，因此每行可能有key对应空值
            for j in range(len(labels)):
                info_dict[labels[j].text] = values[j].text

            info_list.append(info_dict.copy())  # 注意此处要用copy传值

        table_format = {"ID": [], "href": [], "Macromolecule": [], "Released": [], "Method": [],
                        "Resolution": [], "Organisms": [], "Unique Ligands": [], "Unique branched monosaccharides": []}
        # 重构info_dict为表格样式
        for l in info_list:
            table_format["ID"].append(l["ID"])
            table_format["href"].append(l["href"])
            table_format["Released"].append(l["Released"])
            table_format["Macromolecule"].append(l["Macromolecule"])
            table_format["Organisms"].append(l["Organisms"])
            table_format["Unique Ligands"].append(l["Unique Ligands"])
            table_format["Unique branched monosaccharides"].append(l["Unique branched monosaccharides"])

            m = l["Method"]
            r2l_1_space = m.rfind(' ')                  # 从右到左第1个空格
            r2l_2_space = m.rfind(' ', 0, r2l_1_space)  # 从右到左第2个空格
            table_format["Method"].append(m[0:r2l_2_space])
            table_format["Resolution"].append(m[r2l_2_space+1:r2l_1_space])

        df = pd.DataFrame(data=table_format)
        df[['ID', 'Unique Ligands']] = df[['ID', 'Unique Ligands']].astype(str)  # wps脑瘫会自动转换数据格式，用文本编辑器打开是没问题的
        # df['Resolution'] = df['Resolution'].astype(float)  # 存在可能是字符串的情况
        df.to_csv(save_path, header=False, index=False, mode='a')
        print("+", len(info_list), "rows, ", str(page), "/", str(total_page))
        if len(info_list) == 0:
            lost_page.append(page)
    except WebDriverException as wde:
        lost_page.append(page)
        print(str(page), "Exception", wde)

    # 找不到类名为srch-btn pager btn的按钮
    # next_page = browser.find_element(by=By.XPATH,
    #                                  value="//*[@id='app']/div[3]/div[2]/div[3]/div/div[1]/div[3]/div[5]/div[2]/div[3]/div[1]")
    page += 1

print('***finish process***')
print(lost_page)
browser.quit()  # 退出程序，清除内存
