'''
Author       : twips
Date         : 2020-12-05 16:13:46
Description  : 根据api获取图片
LastEditors  : twips
LastEditTime : 2020-12-05 18:02:49
FilePath     : \\spider_mys\\spider_api\\main.py
'''
#%%
import requests
import json
from datetime import datetime


def get_data(start):
    

    params = {
        'forum_id': 4,
        'gids': 19,
        'is_good': 'false',
        'is_hot': 'true',
        'last_id': start,  # 开始id，从这个id开始获取
        'page_size': 20,  # 获取的数量(貌似最多只能40)
    }
    api = 'https://api-takumi.mihoyo.com/post/wapi/getForumPostList'

    res = requests.get(api, params=params)
    res.encoding = 'utf-8'
    result = json.loads(res.text)["data"]
    card_list = result["list"]

    desk = create_dir()
    
    
    for card in card_list:
        # print(count)
        for image in card["image_list"]:
            url = image["url"]
            # name = f'{count + 1}.{image["format"]}'
            name = f'1.{image["format"]}'
            # count = count + 1
            print(url, '~', name)
            # download_img(desk, url, name)
        print('----------------------------')

    print('下载完成')


def create_dir():
    desk = 'C:/Users/Administrator/Desktop/img/' + datetime.now().strftime('%Y-%m-%d %H%M')
    if not os.path.isdir(desk):
        os.makedirs(desk)

    return desk


# 下载图片
def download_img(base_url, img_url, file_name):
    print(img_url)
    print('~~~~~~~~~~~~~~~')
    print(f'{base_url}/{file_name}')
    with open(f'{base_url}/{file_name}', 'wb') as f:
        f.write(requests.get(img_url).content)


# 只能是0和20的倍数
def spider_start(start = 0, end = 40):
    while True:
        if(start >= end):
            break
        
        get_data(start)

        start = start + 20


if __name__ == "__main__":
    spider_start(0, 20)
