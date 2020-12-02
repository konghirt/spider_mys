import sys
import os
from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton
from PyQt5.QtCore import pyqtSlot
from datetime import datetime
import time
import requests
import re
from views.MainWindow import Ui_MainWindow
from utils.mihoyoEnum import *
from script import spider_mihoyo

class MainWin(QMainWindow, Ui_MainWindow):
    
    # 初始化界面
    def __init__(self):

        self.spider_plate = ''  # 板块
        self.spider_type = ''  # 类型
        self.start_num = 1  # 开始张数
        self.scroll_count = 0  # 滚动次数

        super(MainWin, self).__init__()
        self.setupUi(self)

        self.init_data()
        self.addEventListener()

        self.show()
    
    # 事件监听
    def addEventListener(self):
        self.plateBtn1.clicked.connect(self.plate_checked)
        self.plateBtn2.clicked.connect(self.plate_checked)
        self.plateBtn3.clicked.connect(self.plate_checked)
        self.plateBtn4.clicked.connect(self.plate_checked)

        self.typeBtn1.clicked.connect(self.type_checked)
        self.typeBtn2.clicked.connect(self.type_checked)
        self.typeBtn3.clicked.connect(self.type_checked)
        self.typeBtn4.clicked.connect(self.type_checked)

        self.startSpinBox.valueChanged.connect(self.spinBox_start)
        self.countSpinBox.valueChanged.connect(self.spinBox_count)

        self.pushButton.clicked.connect(self.confirm)

    
    # 在文本框打印
    def log(self, str):
        self.textEdit.append(str)
        QApplication.processEvents()  # 刷新界面
    

    # 批量下载
    def download(self, data_list):
        desk = 'C:/Users/Administrator/Desktop/img/' + datetime.now().strftime('%Y-%m-%d %H%M')
        if not os.path.isdir(desk):
            os.makedirs(desk)

        count = 0
        for i, data in enumerate(data_list):
            if i < self.start_num:
                continue
            try:
                img = data['src'].partition('?')[0]
                suffix = re.findall(r'(.jpg|.jpeg|.png|.gif)$', img)[-1]
                file = f'{desk}/{count + 1}{suffix}'
                self.log(f'下载 {img} ...')
                with open(file, 'wb') as f:
                    self.log(f'下载 {img} ...')
                    f.write(requests.get(img).content)
                    count = count + 1
                
                time.sleep(0.5)

            except Exception:
                self.log(f'下载失败, {img}')

        self.log(f'下载完成, 共下载{count}张图片')

    # 执行
    def confirm(self):
        # str = f'{self.spider_plate} {self.spider_type} {self.start_num} {self.scroll_count}'
        self.log('开始爬取...')
        data_list = spider_mihoyo.data_spider(self.spider_plate, self.spider_type, self.scroll_count)
        self.log('爬取完成，开始下载...')
        self.download(data_list)


    # 初始化数据
    def init_data(self):
        self.spinBox_start()
        self.spinBox_count()
        self.plate_checked()
        self.type_checked()
    

    # 开始位置
    def spinBox_start(self):
        self.start_num = self.startSpinBox.value()
        

    # 滚动次数
    def spinBox_count(self):
        self.scroll_count = self.countSpinBox.value()
        if self.scroll_count == '':
            self.scroll_count = 0


    # 板块事件
    def plate_checked(self):

        if self.plateBtn1.isChecked():
            self.spider_plate = GameType.BH2.value

        elif self.plateBtn2.isChecked():
            self.spider_plate = GameType.BH3.value

        elif self.plateBtn3.isChecked():
            self.spider_plate = GameType.YS.value

        elif self.plateBtn4.isChecked():
            self.spider_plate = GameType.DBY.value

    # 类型事件
    def type_checked(self):

        if self.typeBtn1.isChecked():
            self.spider_type = SearchType.LATEST_REPLY.value

        elif self.typeBtn2.isChecked():
            self.spider_type = SearchType.LATEST_RELEASE.value

        elif self.typeBtn3.isChecked():
            self.spider_type = SearchType.HOT.value

        elif self.typeBtn4.isChecked():
            self.spider_type = SearchType.GOOD.value