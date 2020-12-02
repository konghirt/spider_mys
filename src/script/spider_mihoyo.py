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


def data_spider(game, search_type, start_num, scroll_count):

    try:
        # 配置打开的浏览器(需事先启动用于调试的浏览器)
        chrome_options = Options()
        chrome_options.add_experimental_option('debuggerAddress', "127.0.0.1:9222")
        browser = webdriver.Chrome(chrome_options=chrome_options)
    except Exception:
        # print('浏览器打开失败')
        pass
    # # 搜索类型
    # SearchType = {
    #     'LATEST_REPLY': 1,  # 最新回复
    #     'LATEST_RELEASE': 2,  # 最新发帖
    #     'HOT': 'hot',  # 热门
    #     'GOOD': 'good'  # 精华
    # }

    # GameType = {
    #     'BH2': 'https://bbs.mihoyo.com/bh2/home/40',
    #     'BH3': 'https://bbs.mihoyo.com/bh3/home/4',
    #     'YS': 'https://bbs.mihoyo.com/ys/home/29',
    #     'DBY': 'https://bbs.mihoyo.com/dby/home/39'
    # }
    
    # base_url = 'https://bbs.mihoyo.com/bh3/home/4'  # 崩坏3
    # base_url = 'https://bbs.mihoyo.com/ys/home/29'  # 原神
    # base_url = 'https://bbs.mihoyo.com/dby/home/39'  # 大别野
    # base_url = 'https://bbs.mihoyo.com/bh2/home/40'  # 崩坏2

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


def download(data_list):
    desk = 'C:/Users/Administrator/Desktop/img/' + datetime.now().strftime('%Y-%m-%d %H%M')
    if not os.path.isdir(desk):
        os.makedirs(desk)

    for i, data in enumerate(data_list):
        if i < start_num:
            continue
        try:
            img = data['src'].partition('?')[0]
            suffix = re.findall(r'(.jpg|.jpeg|.png|.gif)$', img)[-1]
            # print(f'下载{img}...')
            time.sleep(0.5)
            # with open(f'{desk}/{i + 1}{suffix}', 'wb') as f:
            #     f.write(requests.get(img).content)
        except Exception:
            # print(f'下载失败, {img}')
            pass

    print('下载完成！')


# if __name__ == "__main__":
#     # data_list = data_spider("BH3", "HOT", 3)
#     # download_image(data_list)