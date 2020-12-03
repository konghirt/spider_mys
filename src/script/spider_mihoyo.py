#%%
'''
Description  : 爬取米游社同人图
Author       : twips
Date         : 2020-11-21 10:52:35
LastEditors  : twips
LastEditTime : 2020-12-02 10:25:00
FilePath     : \\flask_test\\src\\spider_mihoyo.py
'''

import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import requests
import time
import re
from datetime import datetime
# import sys


def data_spider(game, search_type, scroll_count):

    try:
        chrome_options = Options()
        # 配置打开的浏览器(需事先启动用于调试的浏览器)
        # chrome_options.add_argument("--user-data-dir="+r"C:/Users/Administrator/AppData/Local/Google/Chrome/User Data")
        # chrome_options.add_experimental_option('debuggerAddress', "127.0.0.1:9222")
        
        browser = webdriver.Chrome(chrome_options=chrome_options)
        
    except Exception:
        print('浏览器打开失败')

    url = f'{game}?type={search_type}'
    # print(url)
    browser.get(url)
    time.sleep(1)

    for index in range(scroll_count):
        browser.execute_script('window.scrollTo(0, document.body.scrollHeight)')
        time.sleep(3)

    soup = BeautifulSoup(browser.page_source, 'html.parser')
    # console.prettify(soup)

    img_card = soup.select('.mhy-img-article-card .mhy-img-article-card__img img')

    return img_card


# def download(data_list):
#     desk = 'C:/Users/Administrator/Desktop/img/' + datetime.now().strftime('%Y-%m-%d %H%M')
#     if not os.path.isdir(desk):
#         os.makedirs(desk)

#     for i, data in enumerate(data_list):
#         try:
#             img = data['src'].partition('?')[0]
#             suffix = re.findall(r'(.jpg|.jpeg|.png|.gif)$', img)[-1]
#             # print(f'下载{img}...')
#             time.sleep(0.5)
#             # with open(f'{desk}/{i + 1}{suffix}', 'wb') as f:
#             #     f.write(requests.get(img).content)
#         except Exception:
#             # print(f'下载失败, {img}')
#             pass

#     print('下载完成！')


# if __name__ == "__main__":
#     # data_list = data_spider("BH3", "HOT", 3)
#     # download_image(data_list)
