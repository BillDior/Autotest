# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\sickk\Documents\GitHub\nostop_Autotest\Autotest\GUI\main_ui_test\test_ui_d\test_ui.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_TestWindow(object):
    def setupUi(self, TestWindow):
        TestWindow.setObjectName("TestWindow")
        TestWindow.resize(1073, 844)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(TestWindow.sizePolicy().hasHeightForWidth())
        TestWindow.setSizePolicy(sizePolicy)
        self.centralwidget = QtWidgets.QWidget(TestWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 350, 1011, 411))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.tabWidget = QtWidgets.QTabWidget(self.layoutWidget)
        self.tabWidget.setObjectName("tabWidget")
        self.queue_list = QtWidgets.QWidget()
        self.queue_list.setObjectName("queue_list")
        self.queueList = QtWidgets.QListWidget(self.queue_list)
        self.queueList.setGeometry(QtCore.QRect(10, 20, 731, 331))
        self.queueList.setObjectName("queueList")
        self.tabWidget.addTab(self.queue_list, "")
        self.report_list = QtWidgets.QWidget()
        self.report_list.setObjectName("report_list")
        self.reportList = QtWidgets.QListWidget(self.report_list)
        self.reportList.setGeometry(QtCore.QRect(10, 20, 731, 331))
        self.reportList.setObjectName("reportList")
        self.tabWidget.addTab(self.report_list, "")
        self.horizontalLayout.addWidget(self.tabWidget)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setSpacing(7)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.loadButton = QtWidgets.QPushButton(self.layoutWidget)
        self.loadButton.setEnabled(False)
        self.loadButton.setMinimumSize(QtCore.QSize(250, 40))
        self.loadButton.setMaximumSize(QtCore.QSize(250, 40))
        self.loadButton.setObjectName("loadButton")
        self.verticalLayout.addWidget(self.loadButton)
        self.saveButton = QtWidgets.QPushButton(self.layoutWidget)
        self.saveButton.setEnabled(False)
        self.saveButton.setMinimumSize(QtCore.QSize(250, 40))
        self.saveButton.setMaximumSize(QtCore.QSize(250, 40))
        self.saveButton.setObjectName("saveButton")
        self.verticalLayout.addWidget(self.saveButton)
        self.startButton = QtWidgets.QPushButton(self.layoutWidget)
        self.startButton.setEnabled(False)
        self.startButton.setMinimumSize(QtCore.QSize(250, 40))
        self.startButton.setMaximumSize(QtCore.QSize(250, 40))
        self.startButton.setObjectName("startButton")
        self.verticalLayout.addWidget(self.startButton)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        self.p_r_s = QtWidgets.QVBoxLayout()
        self.p_r_s.setObjectName("p_r_s")
        self.pauseButton = QtWidgets.QPushButton(self.layoutWidget)
        self.pauseButton.setMinimumSize(QtCore.QSize(250, 40))
        self.pauseButton.setMaximumSize(QtCore.QSize(250, 40))
        self.pauseButton.setObjectName("pauseButton")
        self.p_r_s.addWidget(self.pauseButton)
        self.resumeButton = QtWidgets.QPushButton(self.layoutWidget)
        self.resumeButton.setEnabled(False)
        self.resumeButton.setMinimumSize(QtCore.QSize(250, 40))
        self.resumeButton.setMaximumSize(QtCore.QSize(250, 40))
        self.resumeButton.setObjectName("resumeButton")
        self.p_r_s.addWidget(self.resumeButton)
        self.stopButton = QtWidgets.QPushButton(self.layoutWidget)
        self.stopButton.setMinimumSize(QtCore.QSize(250, 40))
        self.stopButton.setMaximumSize(QtCore.QSize(250, 40))
        self.stopButton.setObjectName("stopButton")
        self.p_r_s.addWidget(self.stopButton)
        self.verticalLayout_2.addLayout(self.p_r_s)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.layoutWidget1 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget1.setGeometry(QtCore.QRect(20, 31, 992, 291))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.layoutWidget1)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.testWinLabel = QtWidgets.QLabel(self.layoutWidget1)
        self.testWinLabel.setMinimumSize(QtCore.QSize(990, 200))
        self.testWinLabel.setMaximumSize(QtCore.QSize(990, 200))
        self.testWinLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.testWinLabel.setObjectName("testWinLabel")
        self.verticalLayout_3.addWidget(self.testWinLabel)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.connectDeviceButton = QtWidgets.QPushButton(self.layoutWidget1)
        self.connectDeviceButton.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.connectDeviceButton.sizePolicy().hasHeightForWidth())
        self.connectDeviceButton.setSizePolicy(sizePolicy)
        self.connectDeviceButton.setMinimumSize(QtCore.QSize(321, 41))
        self.connectDeviceButton.setMaximumSize(QtCore.QSize(321, 41))
        self.connectDeviceButton.setObjectName("connectDeviceButton")
        self.horizontalLayout_2.addWidget(self.connectDeviceButton)
        self.InputAssignmentButton = QtWidgets.QPushButton(self.layoutWidget1)
        self.InputAssignmentButton.setEnabled(False)
        self.InputAssignmentButton.setMinimumSize(QtCore.QSize(321, 41))
        self.InputAssignmentButton.setMaximumSize(QtCore.QSize(321, 41))
        self.InputAssignmentButton.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.InputAssignmentButton.setMouseTracking(False)
        self.InputAssignmentButton.setAutoDefault(False)
        self.InputAssignmentButton.setDefault(False)
        self.InputAssignmentButton.setFlat(False)
        self.InputAssignmentButton.setObjectName("InputAssignmentButton")
        self.horizontalLayout_2.addWidget(self.InputAssignmentButton)
        self.chooseTypeButton = QtWidgets.QPushButton(self.layoutWidget1)
        self.chooseTypeButton.setEnabled(False)
        self.chooseTypeButton.setMinimumSize(QtCore.QSize(321, 41))
        self.chooseTypeButton.setMaximumSize(QtCore.QSize(321, 41))
        self.chooseTypeButton.setObjectName("chooseTypeButton")
        self.horizontalLayout_2.addWidget(self.chooseTypeButton)
        self.verticalLayout_3.addLayout(self.horizontalLayout_2)
        TestWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(TestWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1073, 23))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        TestWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(TestWindow)
        self.statusbar.setObjectName("statusbar")
        TestWindow.setStatusBar(self.statusbar)
        self.menubar.addAction(self.menu.menuAction())

        self.retranslateUi(TestWindow)
        self.tabWidget.setCurrentIndex(0)
        self.chooseTypeButton.clicked.connect(TestWindow.click_add_test)
        self.startButton.clicked.connect(self.loadButton.hide)
        self.startButton.clicked.connect(self.pauseButton.show)
        self.startButton.clicked.connect(self.saveButton.hide)
        self.startButton.clicked.connect(self.saveButton.hide)
        self.startButton.clicked.connect(self.startButton.hide)
        self.startButton.clicked.connect(self.pauseButton.show)
        self.startButton.clicked.connect(self.resumeButton.show)
        self.startButton.clicked.connect(self.stopButton.show)
        self.stopButton.clicked.connect(self.loadButton.show)
        self.stopButton.clicked.connect(self.saveButton.show)
        self.stopButton.clicked.connect(self.startButton.show)
        self.stopButton.clicked.connect(self.pauseButton.hide)
        self.stopButton.clicked.connect(self.resumeButton.hide)
        self.stopButton.clicked.connect(self.stopButton.hide)
        self.loadButton.clicked.connect(TestWindow.click_load_b)
        self.saveButton.clicked.connect(TestWindow.click_save_b)
        self.startButton.clicked.connect(TestWindow.click_start_b)
        self.pauseButton.clicked.connect(TestWindow.click_pause_b)
        self.resumeButton.clicked.connect(TestWindow.click_resume_b)
        self.stopButton.clicked.connect(TestWindow.click_stop_b)
        self.connectDeviceButton.clicked.connect(TestWindow.click_connect_b)
        self.InputAssignmentButton.clicked.connect(TestWindow.click_in_index_b)
        QtCore.QMetaObject.connectSlotsByName(TestWindow)

    def retranslateUi(self, TestWindow):
        _translate = QtCore.QCoreApplication.translate
        TestWindow.setWindowTitle(_translate("TestWindow", "MainWindow"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.queue_list), _translate("TestWindow", "测试队列"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.report_list), _translate("TestWindow", "测试报告"))
        self.loadButton.setText(_translate("TestWindow", "读取存档"))
        self.saveButton.setText(_translate("TestWindow", "保存测试"))
        self.startButton.setText(_translate("TestWindow", "开始测试"))
        self.pauseButton.setText(_translate("TestWindow", "暂停测试"))
        self.resumeButton.setText(_translate("TestWindow", "继续测试"))
        self.stopButton.setText(_translate("TestWindow", "终止测试"))
        self.testWinLabel.setText(_translate("TestWindow", "TextLabel"))
        self.connectDeviceButton.setText(_translate("TestWindow", "连接设备"))
        self.InputAssignmentButton.setText(_translate("TestWindow", "输入要测试的app参数"))
        self.chooseTypeButton.setText(_translate("TestWindow", "选择测试并加入测试队列"))
        self.menu.setTitle(_translate("TestWindow", "帮助"))

