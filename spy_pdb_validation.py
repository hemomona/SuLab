# !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
# File       : spy_pdb_validation.py
# Time       ：2022/6/2 10:48
# Author     ：Jago
# Email      ：18146856052@163.com
# version    ：python 3.7
# Description：
"""
import time

import pyautogui
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
import pandas as pd

xlsx_path = "data/protein_0-2_with_ligands.xlsx"
save_path = r"D:\code\SuLab\data\validation"  # 绝对路径

chrome_option = webdriver.ChromeOptions()
# chrome_option.add_argument('--headless')  # 设置后台运行，不显示浏览器
chrome_option.add_argument("--proxy-server=http://123.172.181.80:5021")  # 设置代理
# pref = {'download.default_directory': save_path}
# chrome_option.add_experimental_option('prefs', pref)  # 设置默认保存路径
browser = webdriver.Chrome(options=chrome_option)
df = pd.read_excel(xlsx_path)

lost_ids = []
lost_hrefs = []
print("***start process***")
for index, row in df.iterrows():
    if index < 27:
        continue
    url = row['href']
    browser.get(url)

    # html中的validation
    img_locator = (By.XPATH, "//div[@class='container']"
                             "/div[@class='tab-content']"
                             "/div[@class='tab-pane active']"
                             "/div[@class='row']"
                             "/div[@class='col-md-8 col-sm-12 col-xs-12']"
                             "/div[@class='row']"
                             "/div[@class='col-sm-7 col-xs-12']"
                             "/div[@class='validation-slider']"
                             "/a/img")

    try:
        validation_img = WebDriverWait(browser, 10).until(
            expected_conditions.presence_of_element_located(img_locator))
        print(index, "image is downloading", validation_img.get_attribute('src'))
        action = ActionChains(browser).move_to_element(validation_img)  # 移动到该图片
        action.context_click(validation_img)  # 右键点击
        action.perform()
        pyautogui.typewrite(['v'])  # 按下v键
        time.sleep(1)
        pyautogui.typewrite(['enter'])
        time.sleep(2)

    except TimeoutError:
        lost_ids.append(row['ID'])
        lost_hrefs.append(row['href'])
        # 这里有问题！！！
        print("!!!", index, "image failed access", validation_img.get_attribute('src'))

    if index == 49:
        break

print('***finish process***')
print("failed access ids:", lost_ids)
print("failed access hrefs:", lost_hrefs)
print("！！！注意：下载的图片集不一定完整，因为偶而有奇怪的点击导致一连串都没下载！！！")
browser.quit()  # 退出程序，清除内存


