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

class SpiderMihoyo:
    
    def __init__(self):
        self.browser = ''

    
    def start(self):
        try:
            chrome_options = Options()
            # 配置打开的浏览器(需事先启动用于调试的浏览器)
            # chrome_options.add_argument("--user-data-dir="+r"C:/Users/Administrator/AppData/Local/Google/Chrome/User Data")
            # chrome_options.add_experimental_option('debuggerAddress', "127.0.0.1:9222")
            
            self.browser = webdriver.Chrome(chrome_options=chrome_options)
            
        except Exception:
            print('浏览器打开失败')

    def data_spider(self, game, search_type, scroll_count):

        url = f'{game}?type={search_type}'
        # print(url)
        self.browser.get(url)
        time.sleep(1)

        for index in range(scroll_count):
            self.browser.execute_script('window.scrollTo(0, document.body.scrollHeight)')
            time.sleep(3)

        soup = BeautifulSoup(self.browser.page_source, 'html.parser')
        # console.prettify(soup)

        img_card = soup.select('.mhy-img-article-card .mhy-img-article-card__img img')

        return img_card


    # 退出
    def quit(self):
        if self.browser:
            self.browser.quit()


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
