#%%
# 使用selenium模拟浏览器行为
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import time

# 配置打开的浏览器(需事先启动用于调试的浏览器)
# dos命令 端口号|配置信息路径 chrome.exe --remote-debugging-port=9222 --user-data-dir="D:\selenium\automationProfile"
chrome_options = Options()
chrome_options.add_experimental_option('debuggerAddress', "127.0.0.1:9222")
browser = webdriver.Chrome(chrome_options=chrome_options)


# url = 'https://search.bilibili.com/all?keyword="vue"'
url = 'https://www.bilibili.com'
browser.get(url)

# browser.maximize_window()  #窗口最大化 确保内容不会被隐藏
browser.find_element_by_class_name('nav-search-keyword').send_keys('java')
browser.find_element_by_class_name('nav-search-submit').click()
time.sleep(1)

# 获取所有窗口的句柄
handles = browser.window_handles
print(handles)

# 切换到新打开的窗口
browser.switch_to.window(browser.window_handles[-1])

# print(browser.current_window_handle)

# 滚动到底部
# browser.execute_script('window.scrollTo(0, document.body.scrollHeight)')
# print(browser.title)

soup = BeautifulSoup(browser.page_source, 'html.parser')
video_list = soup.select('.video-list .video-item')

list = []
for video in video_list:
    # print(video.prettify())
    # list.append(video.select('.headline a')[0].text)
    # print(video.parent)
    obj = {
        'img': video.find('img')['src'],
        'video_href': video.find('a')['href'],
        'title': video.find('a')['title']
    }
    list.append(obj)
    print(obj)
    print('-----------------------')

# print(browser.page_source)
# browser.close()


#%%
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import requests
import time
import re
from datetime import datetime

# browser = None

def init(keyword="vue"):
    chrome_options = Options()
    chrome_options.add_experimental_option('debuggerAddress', "127.0.0.1:9222")
    browser = webdriver.Chrome(chrome_options=chrome_options)
    url = f'https://search.bilibili.com/all?keyword={keyword}'
    # url = 'https://www.bilibili.com'
    browser.get(url)
    browser.maximize_window()  #窗口最大化 确保内容不会被隐藏
    return browser


def get_html(browser):
    soup = BeautifulSoup(browser.page_source, 'html.parser')
    video_list = soup.select('.video-list .video-item')
    img_list = []
    for video in video_list:
        # print(video.prettify())
        # list.append(video.select('.headline a')[0].text)
        # print(video.parent)
        img_url = 'http:' + video.find('img')['src'].replace('@320w_200h.webp', '')
        suffix = re.findall(r'(.jpg|.png)$', img_url)[-1]
        # print('suffix: ', suffix)

        obj = {
            'img_url': img_url,
            'suffix': suffix
        }

        img_list.append(obj)
        # print('-----------------------')

    return img_list


# 下一页
def go_next():
    browser.find_element_by_css_selector(".nav-btn.iconfont.icon-arrowdown3").click()


def download_img(base_url, img_url, file_name):
    print(img_url)
    with open(f'{base_url}/{file_name}', 'wb') as f:
        f.write(requests.get(img_url).content)
    

# 点击下一页
# browser.find_element_by_css_selector(".nav-btn.iconfont.icon-arrowdown3").click()

if __name__ == "__main__":
    #  文件保存位置
    desk = 'C:/Users/Administrator/Desktop/img/' + datetime.now().strftime('%Y-%m-%d %H%M')
    if not os.path.isdir(desk):
        os.makedirs(desk)

    browser = init()
    # get_html(browser)
    for page in range(1, 2):
        img_list = get_html(browser)
        for i, img in enumerate(img_list):
            # print(img)
            download_img(desk, img['img_url'], f'{i + 1}{img["suffix"]}')

    print('下载完成')



#%%
import re

str = '//i2.hdslb.com/bfs/archive/b1b39b6bb046f05940bc3232ede968870b06b10a.jpg@320w_200h.webp'

# print(str.replace('^/.', ''))
print(re.findall(r'(.jpg)', str))


#%%
# ------
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import requests
import time
import re
from datetime import datetime


# 配置打开的浏览器(需事先启动用于调试的浏览器)
chrome_options = Options()
chrome_options.add_experimental_option('debuggerAddress', "127.0.0.1:9222")
browser = webdriver.Chrome(chrome_options=chrome_options)

url = 'https://h.bilibili.com/eden/draw_area#/all/hot'
browser.get(url)


for index in range(3):
    browser.execute_script('window.scrollTo(0, document.body.scrollHeight)')
    time.sleep(3)


soup = BeautifulSoup(browser.page_source, 'html.parser')
# print(soup)

img_list = soup.select('.content .img-contain')
# print(img_list)


desk = 'C:/Users/Administrator/Desktop/img/' + datetime.now().strftime('%Y-%m-%d %H%M')
if not os.path.isdir(desk):
    os.makedirs(desk)

for i,img_obj in enumerate(img_list):
    img = re.match('.*(?=@)', img_obj['data-src']).group()
    suffix = re.findall(r'(.jpg|.png)$', img)[-1]
    print(f'下载{img}...')
    time.sleep(1)
    with open(f'{desk}/{i}{suffix}', 'wb') as f:
        f.write(requests.get(img).content)

print('下载完成！')




# for script in soup.findAll('script'):
#     script.extract()

# for style in soup.findAll('style'):
#     style.extract()

# print(soup.prettify())

#%%
import re

str = 'https://i0.hdslb.com/bfs/album/f6bfea5528fd49a52f7d189f464dcd4f896786bd.jpg'
re.findall(r'(.jpg|.png)$', str)[-1]