'''
Author       : twips
Date         : 2020-12-05 16:13:46
Description  : 根据api获取图片
LastEditors  : twips
LastEditTime : 2020-12-19 16:38:43
FilePath     : \\spider_mys\\spider_api\\main.py
'''
#%%
import requests
import json
from datetime import datetime

class MHY:
    
    def __init__(self):
        self.count = 1

    def get_data(self, start):

        # 热门所需参数
        params = {
            'forum_id': 4,
            'gids': 1,
            'is_good': 'false',
            'is_hot': 'true',
            'last_id': start,  # 开始id，从这个id开始获取
            'page_size': 20,  # 获取的数量(貌似最多只能40)
        }

        # 最新回复
        # params = {
        #     'forum_id': 4,
        #     'gids': 1,
        #     'page_size': 20,
        # }
        
        api = 'https://api-takumi.mihoyo.com/post/wapi/getForumPostList'

        res = requests.get(api, params=params)
        res.encoding = 'utf-8'
        result = json.loads(res.text)["data"]
        card_list = result["list"]

        # print_json(card_list)
        # return

        # 新建文件夹
        desk = self.create_dir()
        
        for card in card_list:
            # print(count)
            for image in card["image_list"]:
                url = image["url"]
                # name = f'{count + 1}.{image["format"]}'
                name = f'{self.count}.{image["format"]}'
                self.count = self.count + 1
                print(url, '~', name)
                self.download_img(desk, url, name)
            print('----------------------------')

        print('下载完成')


    def create_dir(self):
        desk = 'C:/Users/Administrator/Desktop/img/' + datetime.now().strftime('%Y-%m-%d %H%M')
        if not os.path.isdir(desk):
            os.makedirs(desk)

        return desk


    # 下载图片
    def download_img(self, base_url, img_url, file_name):
        # print(img_url)
        # print('~~~~~~~~~~~~~~~')
        # print(f'{base_url}/{file_name}')
        with open(f'{base_url}/{file_name}', 'wb') as f:
            f.write(requests.get(img_url).content)


    # 只能是0和20的倍数
    def spider_start(self, start = 0, end = 40):
        while True:
            if(start >= end):
                break
            
            self.get_data(start)

            start = start + 20


def print_json(data):
    print(json.dumps(data, sort_keys=True, indent=4, separators=(', ', ': '), ensure_ascii=False))


if __name__ == "__main__":
    mhy = MHY()
    mhy.spider_start(0, 40)
