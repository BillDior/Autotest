# -*- coding: utf-8 -*-
#因为文件不齐，现在只能把加进的函数注释掉才能看到界面
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtWidgets import QFileDialog, QMessageBox, QDockWidget, QListWidget
from PyQt5.QtGui import *
#from Test_Ui_Functions import *
import Test_Ui_Functions as funcs
from Ui_test_ui_1 import Ui_TestWindow #import刚刚创建的GUI类
class myTestWindow(QtWidgets.QMainWindow,Ui_TestWindow):
    def __init__(self):#因为是继承自Qtwidgets.QMainWindow和Ui_MainWindow的，重载一下父类构造函数
        super(myTestWindow,self).__init__()
        self.setupUi(self) #初始化UI界面
        self.queueList.setDragDropMode(self.queueList.InternalMove)
        self.queueList.setAcceptDrops(True)
        for i in range(0,5):
            self.queueList.addItem(str((i * 753 + 33) % 14))
        self.queueList.addItem("world")


if  __name__ == '__main__': #python的main函数
    app = QtWidgets.QApplication(sys.argv)
    # QApplication相当于main函数，也就是整个程序（很多文件）的主入口函数。
    # 对于GUI程序必须至少有一个这样的实例来让程序运行。
    test_window = myTestWindow()
    test_window.show()
    fuctions_class = funcs.TestUiFunctionsClass()
    fuctions_class.add_text("12345",test_window.queueList)
    #close_monkeyrunner()
    #close_model()
    sys.exit(app.exec_()) #正常退出程序