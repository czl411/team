# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'team.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.
import sys

from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMainWindow

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1200, 710)
        MainWindow.setMinimumSize(QtCore.QSize(1200, 710))
        MainWindow.setMaximumSize(QtCore.QSize(1200, 710))
        MainWindow.setStyleSheet("background-image: url(:/test/VCG41N667816120.jpg);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setMinimumSize(QtCore.QSize(1200, 710))
        self.centralwidget.setMaximumSize(QtCore.QSize(1200, 710))
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(0, 0, 1200, 710))
        self.frame.setMaximumSize(QtCore.QSize(1201, 770))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(880, 120, 171, 21))
        self.label.setStyleSheet("selection-background-color: rgb(255, 255, 255);\n"
"color: rgb(255, 255, 255);")
        self.label.setObjectName("label")
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.frame)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(1000, 50, 197, 61))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.pushButton_6 = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.pushButton_6.setStyleSheet("color: rgb(255, 255, 255);")
        self.pushButton_6.setObjectName("pushButton_6")
        self.horizontalLayout_3.addWidget(self.pushButton_6)
        self.pushButton_7 = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.pushButton_7.setStyleSheet("color: rgb(255, 255, 255);")
        self.pushButton_7.setObjectName("pushButton_7")
        self.horizontalLayout_3.addWidget(self.pushButton_7)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.radioButton_3 = QtWidgets.QRadioButton(self.verticalLayoutWidget_2)
        self.radioButton_3.setStyleSheet("color: rgb(255, 255, 255);")
        self.radioButton_3.setObjectName("radioButton_3")
        self.verticalLayout_2.addWidget(self.radioButton_3)
        self.plainTextEdit_8 = QtWidgets.QPlainTextEdit(self.frame)
        self.plainTextEdit_8.setGeometry(QtCore.QRect(880, 390, 321, 231))
        self.plainTextEdit_8.setObjectName("plainTextEdit_8")
        self.horizontalLayoutWidget_5 = QtWidgets.QWidget(self.frame)
        self.horizontalLayoutWidget_5.setGeometry(QtCore.QRect(940, 670, 251, 31))
        self.horizontalLayoutWidget_5.setObjectName("horizontalLayoutWidget_5")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_5)
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5.setSpacing(1)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.pushButton_20 = QtWidgets.QPushButton(self.horizontalLayoutWidget_5)
        self.pushButton_20.setMaximumSize(QtCore.QSize(20, 20))
        self.pushButton_20.setStyleSheet("color: rgb(255, 255, 255);")
        self.pushButton_20.setObjectName("pushButton_20")
        self.horizontalLayout_5.addWidget(self.pushButton_20)
        self.pushButton_23 = QtWidgets.QPushButton(self.horizontalLayoutWidget_5)
        self.pushButton_23.setMaximumSize(QtCore.QSize(20, 20))
        self.pushButton_23.setStyleSheet("color: rgb(255, 255, 255);")
        self.pushButton_23.setObjectName("pushButton_23")
        self.horizontalLayout_5.addWidget(self.pushButton_23)
        self.pushButton_25 = QtWidgets.QPushButton(self.horizontalLayoutWidget_5)
        self.pushButton_25.setMaximumSize(QtCore.QSize(20, 20))
        self.pushButton_25.setStyleSheet("color: rgb(255, 255, 255);")
        self.pushButton_25.setObjectName("pushButton_25")
        self.horizontalLayout_5.addWidget(self.pushButton_25)
        self.pushButton_11 = QtWidgets.QPushButton(self.horizontalLayoutWidget_5)
        self.pushButton_11.setMaximumSize(QtCore.QSize(20, 20))
        self.pushButton_11.setStyleSheet("color: rgb(255, 255, 255);")
        self.pushButton_11.setObjectName("pushButton_11")
        self.horizontalLayout_5.addWidget(self.pushButton_11)
        self.pushButton_21 = QtWidgets.QPushButton(self.horizontalLayoutWidget_5)
        self.pushButton_21.setMaximumSize(QtCore.QSize(20, 20))
        self.pushButton_21.setStyleSheet("color: rgb(255, 255, 255);")
        self.pushButton_21.setObjectName("pushButton_21")
        self.horizontalLayout_5.addWidget(self.pushButton_21)
        self.pushButton_24 = QtWidgets.QPushButton(self.horizontalLayoutWidget_5)
        self.pushButton_24.setMaximumSize(QtCore.QSize(20, 20))
        self.pushButton_24.setStyleSheet("color: rgb(255, 255, 255);")
        self.pushButton_24.setObjectName("pushButton_24")
        self.horizontalLayout_5.addWidget(self.pushButton_24)
        self.pushButton_22 = QtWidgets.QPushButton(self.horizontalLayoutWidget_5)
        self.pushButton_22.setMaximumSize(QtCore.QSize(20, 20))
        self.pushButton_22.setStyleSheet("color: rgb(255, 255, 255);")
        self.pushButton_22.setObjectName("pushButton_22")
        self.horizontalLayout_5.addWidget(self.pushButton_22)
        self.pushButton_26 = QtWidgets.QPushButton(self.horizontalLayoutWidget_5)
        self.pushButton_26.setMaximumSize(QtCore.QSize(20, 20))
        self.pushButton_26.setStyleSheet("color: rgb(255, 255, 255);")
        self.pushButton_26.setObjectName("pushButton_26")
        self.horizontalLayout_5.addWidget(self.pushButton_26)
        self.horizontalLayoutWidget_6 = QtWidgets.QWidget(self.frame)
        self.horizontalLayoutWidget_6.setGeometry(QtCore.QRect(1060, 630, 122, 31))
        self.horizontalLayoutWidget_6.setObjectName("horizontalLayoutWidget_6")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_6)
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.pushButton_27 = QtWidgets.QPushButton(self.horizontalLayoutWidget_6)
        self.pushButton_27.setStyleSheet("color: rgb(255, 255, 255);")
        self.pushButton_27.setObjectName("pushButton_27")
        self.horizontalLayout_6.addWidget(self.pushButton_27)
        self.pushButton_28 = QtWidgets.QPushButton(self.horizontalLayoutWidget_6)
        self.pushButton_28.setMaximumSize(QtCore.QSize(20, 20))
        self.pushButton_28.setStyleSheet("color: rgb(255, 255, 255);")
        self.pushButton_28.setObjectName("pushButton_28")
        self.horizontalLayout_6.addWidget(self.pushButton_28)
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(880, 370, 171, 21))
        self.label_2.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_2.setObjectName("label_2")
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.frame)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(0, 680, 195, 31))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.pushButton_4 = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        self.pushButton_4.setStyleSheet("color: rgb(255, 255, 255);")
        self.pushButton_4.setObjectName("pushButton_4")
        self.horizontalLayout_2.addWidget(self.pushButton_4)
        self.pushButton_5 = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        self.pushButton_5.setStyleSheet("color: rgb(255, 255, 255);")
        self.pushButton_5.setObjectName("pushButton_5")
        self.horizontalLayout_2.addWidget(self.pushButton_5)
        self.plainTextEdit_7 = QtWidgets.QPlainTextEdit(self.frame)
        self.plainTextEdit_7.setGeometry(QtCore.QRect(880, 140, 321, 231))
        self.plainTextEdit_7.setObjectName("plainTextEdit_7")
        self.tabWidget_2 = QtWidgets.QTabWidget(self.frame)
        self.tabWidget_2.setGeometry(QtCore.QRect(180, 50, 691, 571))
        self.tabWidget_2.setObjectName("tabWidget_2")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.plainTextEdit = QtWidgets.QPlainTextEdit(self.tab_4)
        self.plainTextEdit.setGeometry(QtCore.QRect(150, 140, 104, 87))
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.tabWidget_2.addTab(self.tab_4, "")
        self.tab_5 = QtWidgets.QWidget()
        self.tab_5.setObjectName("tab_5")
        self.plainTextEdit_2 = QtWidgets.QPlainTextEdit(self.tab_5)
        self.plainTextEdit_2.setGeometry(QtCore.QRect(160, 140, 104, 87))
        self.plainTextEdit_2.setObjectName("plainTextEdit_2")
        self.tabWidget_2.addTab(self.tab_5, "")
        self.tab_6 = QtWidgets.QWidget()
        self.tab_6.setObjectName("tab_6")
        self.plainTextEdit_3 = QtWidgets.QPlainTextEdit(self.tab_6)
        self.plainTextEdit_3.setGeometry(QtCore.QRect(150, 230, 104, 87))
        self.plainTextEdit_3.setObjectName("plainTextEdit_3")
        self.tabWidget_2.addTab(self.tab_6, "")
        self.horizontalLayoutWidget_7 = QtWidgets.QWidget(self.frame)
        self.horizontalLayoutWidget_7.setGeometry(QtCore.QRect(190, 630, 195, 31))
        self.horizontalLayoutWidget_7.setObjectName("horizontalLayoutWidget_7")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_7)
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.pushButton_18 = QtWidgets.QPushButton(self.horizontalLayoutWidget_7)
        self.pushButton_18.setStyleSheet("color: rgb(255, 255, 255);")
        self.pushButton_18.setObjectName("pushButton_18")
        self.horizontalLayout_7.addWidget(self.pushButton_18)
        self.pushButton_19 = QtWidgets.QPushButton(self.horizontalLayoutWidget_7)
        self.pushButton_19.setStyleSheet("color: rgb(255, 255, 255);")
        self.pushButton_19.setObjectName("pushButton_19")
        self.horizontalLayout_7.addWidget(self.pushButton_19)
        self.tabWidget = QtWidgets.QTabWidget(self.frame)
        self.tabWidget.setGeometry(QtCore.QRect(0, 50, 181, 631))
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.tab)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 171, 121))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.horizontalLayout_15 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_15.setObjectName("horizontalLayout_15")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.lineEdit_3.setMaximumSize(QtCore.QSize(100, 16777215))
        self.lineEdit_3.setStyleSheet("color: rgb(255, 255, 255);")
        self.lineEdit_3.setInputMask("")
        self.lineEdit_3.setText("")
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.horizontalLayout_15.addWidget(self.lineEdit_3)
        self.pushButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy)
        self.pushButton.setMaximumSize(QtCore.QSize(40, 16777215))
        self.pushButton.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(255, 255, 255);")
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout_15.addWidget(self.pushButton)
        self.horizontalLayout.addLayout(self.horizontalLayout_15)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.comboBox = QtWidgets.QComboBox(self.verticalLayoutWidget)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.verticalLayout.addWidget(self.comboBox)
        self.comboBox_3 = QtWidgets.QComboBox(self.verticalLayoutWidget)
        self.comboBox_3.setObjectName("comboBox_3")
        self.comboBox_3.addItem("")
        self.verticalLayout.addWidget(self.comboBox_3)
        self.comboBox_2 = QtWidgets.QComboBox(self.verticalLayoutWidget)
        self.comboBox_2.setEditable(False)
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.verticalLayout.addWidget(self.comboBox_2)
        self.toolBox = QtWidgets.QToolBox(self.tab)
        self.toolBox.setGeometry(QtCore.QRect(0, 140, 171, 241))
        self.toolBox.setObjectName("toolBox")
        self.page = QtWidgets.QWidget()
        self.page.setGeometry(QtCore.QRect(0, 0, 100, 30))
        self.page.setObjectName("page")
        self.toolBox.addItem(self.page, "")
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setGeometry(QtCore.QRect(0, 0, 100, 30))
        self.page_2.setObjectName("page_2")
        self.toolBox.addItem(self.page_2, "")
        self.page_3 = QtWidgets.QWidget()
        self.page_3.setGeometry(QtCore.QRect(0, 0, 171, 151))
        self.page_3.setObjectName("page_3")
        self.toolBox.addItem(self.page_3, "")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.pushButton_2 = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_2.setGeometry(QtCore.QRect(30, 180, 93, 28))
        self.pushButton_2.setObjectName("pushButton_2")
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.pushButton_3 = QtWidgets.QPushButton(self.tab_3)
        self.pushButton_3.setGeometry(QtCore.QRect(30, 250, 93, 28))
        self.pushButton_3.setObjectName("pushButton_3")
        self.tabWidget.addTab(self.tab_3, "")
        self.horizontalLayoutWidget_4 = QtWidgets.QWidget(self.frame)
        self.horizontalLayoutWidget_4.setGeometry(QtCore.QRect(190, 670, 295, 31))
        self.horizontalLayoutWidget_4.setObjectName("horizontalLayoutWidget_4")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_4)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.pushButton_9 = QtWidgets.QPushButton(self.horizontalLayoutWidget_4)
        self.pushButton_9.setStyleSheet("color: rgb(255, 255, 255);")
        self.pushButton_9.setObjectName("pushButton_9")
        self.horizontalLayout_4.addWidget(self.pushButton_9)
        self.pushButton_8 = QtWidgets.QPushButton(self.horizontalLayoutWidget_4)
        self.pushButton_8.setStyleSheet("color: rgb(255, 255, 255);")
        self.pushButton_8.setObjectName("pushButton_8")
        self.horizontalLayout_4.addWidget(self.pushButton_8)
        self.pushButton_10 = QtWidgets.QPushButton(self.horizontalLayoutWidget_4)
        self.pushButton_10.setStyleSheet("color: rgb(255, 255, 255);")
        self.pushButton_10.setObjectName("pushButton_10")
        self.horizontalLayout_4.addWidget(self.pushButton_10)
        self.toolButton = QtWidgets.QToolButton(self.frame)
        self.toolButton.setGeometry(QtCore.QRect(870, 10, 47, 21))
        self.toolButton.setStyleSheet("color: rgb(255, 255, 255);")
        self.toolButton.setObjectName("toolButton")
        self.toolButton_2 = QtWidgets.QToolButton(self.frame)
        self.toolButton_2.setGeometry(QtCore.QRect(930, 10, 47, 21))
        self.toolButton_2.setStyleSheet("color: rgb(255, 255, 255);")
        self.toolButton_2.setObjectName("toolButton_2")
        self.toolButton_3 = QtWidgets.QToolButton(self.frame)
        self.toolButton_3.setGeometry(QtCore.QRect(990, 10, 47, 21))
        self.toolButton_3.setStyleSheet("color: rgb(255, 255, 255);")
        self.toolButton_3.setObjectName("toolButton_3")
        self.toolButton_5 = QtWidgets.QToolButton(self.frame)
        self.toolButton_5.setGeometry(QtCore.QRect(1040, 10, 47, 21))
        self.toolButton_5.setStyleSheet("color: rgb(255, 255, 255);")
        self.toolButton_5.setObjectName("toolButton_5")
        self.toolButton_6 = QtWidgets.QToolButton(self.frame)
        self.toolButton_6.setGeometry(QtCore.QRect(1090, 10, 47, 21))
        self.toolButton_6.setStyleSheet("color: rgb(255, 255, 255);")
        self.toolButton_6.setObjectName("toolButton_6")
        self.toolButton_7 = QtWidgets.QToolButton(self.frame)
        self.toolButton_7.setGeometry(QtCore.QRect(1140, 10, 47, 21))
        self.toolButton_7.setStyleSheet("color: rgb(255, 255, 255);")
        self.toolButton_7.setObjectName("toolButton_7")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.tabWidget_2.setCurrentIndex(0)
        self.tabWidget.setCurrentIndex(0)
        self.toolBox.setCurrentIndex(2)
        self.toolButton_2.clicked.connect(MainWindow.close) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "垃圾存放点信息输出"))
        self.pushButton_6.setText(_translate("MainWindow", "云存储"))
        self.pushButton_7.setText(_translate("MainWindow", "意见留言"))
        self.radioButton_3.setText(_translate("MainWindow", "展示窗口序号"))
        self.pushButton_20.setText(_translate("MainWindow", "1"))
        self.pushButton_23.setText(_translate("MainWindow", "1"))
        self.pushButton_25.setText(_translate("MainWindow", "1"))
        self.pushButton_11.setText(_translate("MainWindow", "1"))
        self.pushButton_21.setText(_translate("MainWindow", "1"))
        self.pushButton_24.setText(_translate("MainWindow", "1"))
        self.pushButton_22.setText(_translate("MainWindow", "1"))
        self.pushButton_26.setText(_translate("MainWindow", "1"))
        self.pushButton_27.setText(_translate("MainWindow", "开启轮巡"))
        self.pushButton_28.setText(_translate("MainWindow", "0"))
        self.label_2.setText(_translate("MainWindow", "行人行为信息输出"))
        self.pushButton_4.setText(_translate("MainWindow", "设备管理"))
        self.pushButton_5.setText(_translate("MainWindow", "添加"))
        self.plainTextEdit.setPlainText(_translate("MainWindow", "1"))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_4), _translate("MainWindow", "第一屏"))
        self.plainTextEdit_2.setPlainText(_translate("MainWindow", "2"))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_5), _translate("MainWindow", "第二屏"))
        self.plainTextEdit_3.setPlainText(_translate("MainWindow", "3"))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_6), _translate("MainWindow", "第三屏"))
        self.pushButton_18.setText(_translate("MainWindow", "PushButton"))
        self.pushButton_19.setText(_translate("MainWindow", "PushButton"))
        self.lineEdit_3.setPlaceholderText(_translate("MainWindow", "搜索：设备名"))
        self.pushButton.setText(_translate("MainWindow", "搜索"))
        self.comboBox.setItemText(0, _translate("MainWindow", "我的设备"))
        self.comboBox_3.setItemText(0, _translate("MainWindow", "默认分组"))
        self.comboBox_2.setItemText(0, _translate("MainWindow", "本地设备"))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page), _translate("MainWindow", "我的设备"))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_2), _translate("MainWindow", "默认分组"))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_3), _translate("MainWindow", "本地设备"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "用户"))
        self.pushButton_2.setText(_translate("MainWindow", "PushButton"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "信息"))
        self.pushButton_3.setText(_translate("MainWindow", "PushButton"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("MainWindow", "功能"))
        self.pushButton_9.setText(_translate("MainWindow", "卡录像"))
        self.pushButton_8.setText(_translate("MainWindow", "预览"))
        self.pushButton_10.setText(_translate("MainWindow", "云录像"))
        self.toolButton.setText(_translate("MainWindow", "root"))
        self.toolButton_2.setText(_translate("MainWindow", "退出"))
        self.toolButton_3.setText(_translate("MainWindow", "菜单"))
        self.toolButton_5.setText(_translate("MainWindow", "-"))
        self.toolButton_6.setText(_translate("MainWindow", "口"))
        self.toolButton_7.setText(_translate("MainWindow", "×"))
import resource_rc
if __name__ == '__main__':  # 程序的入口
    app = QApplication(sys.argv)
    mainwindow = QMainWindow()
    win = Ui_MainWindow()
    win.setupUi(mainwindow)
    mainwindow.show()
    sys.exit(app.exec_())