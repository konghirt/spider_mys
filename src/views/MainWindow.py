# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'a.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setFixedSize(638, 446)
        MainWindow.setAnimated(True)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.clearBtn = QtWidgets.QPushButton(self.centralwidget)
        self.clearBtn.setGeometry(QtCore.QRect(550, 380, 71, 23))
        self.clearBtn.setObjectName("clearBtn")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(550, 130, 71, 23))
        self.pushButton.setObjectName("pushButton")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(24, 99, 244, 22))
        self.widget.setObjectName("widget")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.widget)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.label_5 = QtWidgets.QLabel(self.widget)
        self.label_5.setObjectName("label_5")
        self.gridLayout_3.addWidget(self.label_5, 0, 0, 1, 1)
        self.startSpinBox = QtWidgets.QSpinBox(self.widget)
        self.startSpinBox.setMinimum(1)
        self.startSpinBox.setObjectName("startSpinBox")
        self.gridLayout_3.addWidget(self.startSpinBox, 0, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.widget)
        self.label_3.setObjectName("label_3")
        self.gridLayout_3.addWidget(self.label_3, 0, 2, 1, 1)
        self.countSpinBox = QtWidgets.QSpinBox(self.widget)
        self.countSpinBox.setObjectName("countSpinBox")
        self.gridLayout_3.addWidget(self.countSpinBox, 0, 3, 1, 1)
        self.widget1 = QtWidgets.QWidget(self.centralwidget)
        self.widget1.setGeometry(QtCore.QRect(20, 160, 601, 212))
        self.widget1.setObjectName("widget1")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.widget1)
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.label_4 = QtWidgets.QLabel(self.widget1)
        self.label_4.setObjectName("label_4")
        self.gridLayout_4.addWidget(self.label_4, 0, 0, 1, 1)
        self.textEdit = QtWidgets.QTextEdit(self.widget1)
        self.textEdit.setReadOnly(True)
        self.textEdit.setPlaceholderText("")
        self.textEdit.setObjectName("textEdit")
        self.gridLayout_4.addWidget(self.textEdit, 1, 0, 1, 1)
        self.widget2 = QtWidgets.QWidget(self.centralwidget)
        self.widget2.setGeometry(QtCore.QRect(21, 0, 431, 41))
        self.widget2.setObjectName("widget2")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.widget2)
        self.gridLayout_5.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.label = QtWidgets.QLabel(self.widget2)
        self.label.setMaximumSize(QtCore.QSize(24, 16777215))
        self.label.setObjectName("label")
        self.gridLayout_5.addWidget(self.label, 0, 0, 1, 1)
        self.groupBox = QtWidgets.QGroupBox(self.widget2)
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.widget3 = QtWidgets.QWidget(self.groupBox)
        self.widget3.setGeometry(QtCore.QRect(10, 10, 381, 18))
        self.widget3.setObjectName("widget3")
        self.gridLayout = QtWidgets.QGridLayout(self.widget3)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.plateBtn3 = QtWidgets.QRadioButton(self.widget3)
        self.plateBtn3.setChecked(True)
        self.plateBtn3.setObjectName("plateBtn3")
        self.gridLayout.addWidget(self.plateBtn3, 0, 2, 1, 1)
        self.plateBtn2 = QtWidgets.QRadioButton(self.widget3)
        self.plateBtn2.setObjectName("plateBtn2")
        self.gridLayout.addWidget(self.plateBtn2, 0, 1, 1, 1)
        self.plateBtn4 = QtWidgets.QRadioButton(self.widget3)
        self.plateBtn4.setObjectName("plateBtn4")
        self.gridLayout.addWidget(self.plateBtn4, 0, 3, 1, 1)
        self.plateBtn1 = QtWidgets.QRadioButton(self.widget3)
        self.plateBtn1.setObjectName("plateBtn1")
        self.gridLayout.addWidget(self.plateBtn1, 0, 0, 1, 1)
        self.gridLayout_5.addWidget(self.groupBox, 0, 1, 1, 1)
        self.widget4 = QtWidgets.QWidget(self.centralwidget)
        self.widget4.setGeometry(QtCore.QRect(21, 50, 431, 41))
        self.widget4.setObjectName("widget4")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.widget4)
        self.gridLayout_6.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.label_2 = QtWidgets.QLabel(self.widget4)
        self.label_2.setMaximumSize(QtCore.QSize(24, 16777215))
        self.label_2.setObjectName("label_2")
        self.gridLayout_6.addWidget(self.label_2, 0, 0, 1, 1)
        self.groupBox_2 = QtWidgets.QGroupBox(self.widget4)
        self.groupBox_2.setTitle("")
        self.groupBox_2.setObjectName("groupBox_2")
        self.widget5 = QtWidgets.QWidget(self.groupBox_2)
        self.widget5.setGeometry(QtCore.QRect(11, 11, 381, 18))
        self.widget5.setObjectName("widget5")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.widget5)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.typeBtn1 = QtWidgets.QRadioButton(self.widget5)
        self.typeBtn1.setChecked(False)
        self.typeBtn1.setObjectName("typeBtn1")
        self.gridLayout_2.addWidget(self.typeBtn1, 0, 0, 1, 1)
        self.typeBtn2 = QtWidgets.QRadioButton(self.widget5)
        self.typeBtn2.setObjectName("typeBtn2")
        self.gridLayout_2.addWidget(self.typeBtn2, 0, 1, 1, 1)
        self.typeBtn3 = QtWidgets.QRadioButton(self.widget5)
        self.typeBtn3.setObjectName("typeBtn3")
        self.gridLayout_2.addWidget(self.typeBtn3, 0, 2, 1, 1)
        self.typeBtn4 = QtWidgets.QRadioButton(self.widget5)
        self.typeBtn4.setChecked(True)
        self.typeBtn4.setObjectName("typeBtn4")
        self.gridLayout_2.addWidget(self.typeBtn4, 0, 3, 1, 1)
        self.gridLayout_6.addWidget(self.groupBox_2, 0, 1, 1, 1)
        self.widget6 = QtWidgets.QWidget(self.centralwidget)
        self.widget6.setGeometry(QtCore.QRect(21, 130, 431, 25))
        self.widget6.setObjectName("widget6")
        self.gridLayout_7 = QtWidgets.QGridLayout(self.widget6)
        self.gridLayout_7.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.saveEditText = QtWidgets.QLineEdit(self.widget6)
        self.saveEditText.setText("")
        self.saveEditText.setObjectName("saveEditText")
        self.gridLayout_7.addWidget(self.saveEditText, 0, 1, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.widget6)
        self.label_6.setObjectName("label_6")
        self.gridLayout_7.addWidget(self.label_6, 0, 0, 1, 1)
        self.chooseFileBtn = QtWidgets.QPushButton(self.widget6)
        self.chooseFileBtn.setObjectName("chooseFileBtn")
        self.gridLayout_7.addWidget(self.chooseFileBtn, 0, 2, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "图片爬取"))
        self.clearBtn.setText(_translate("MainWindow", "清空"))
        self.pushButton.setText(_translate("MainWindow", "执行"))
        self.label_5.setText(_translate("MainWindow", "从第几张开始"))
        self.label_3.setText(_translate("MainWindow", "    滚动次数"))
        self.label_4.setText(_translate("MainWindow", "结果"))
        self.textEdit.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.label.setText(_translate("MainWindow", "板块"))
        self.plateBtn3.setText(_translate("MainWindow", "YS"))
        self.plateBtn2.setText(_translate("MainWindow", "BH3"))
        self.plateBtn4.setText(_translate("MainWindow", "DBY"))
        self.plateBtn1.setText(_translate("MainWindow", "BH2"))
        self.label_2.setText(_translate("MainWindow", "类型"))
        self.typeBtn1.setText(_translate("MainWindow", "最新回复"))
        self.typeBtn2.setText(_translate("MainWindow", "最新发帖"))
        self.typeBtn3.setText(_translate("MainWindow", "热门"))
        self.typeBtn4.setText(_translate("MainWindow", "精华"))
        self.label_6.setText(_translate("MainWindow", "下载位置"))
        self.chooseFileBtn.setText(_translate("MainWindow", "选择"))
