# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Game.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(297, 300)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Desktop/骰子图标.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Form.setWindowIcon(icon)
        self.StartGame = QtWidgets.QPushButton(Form)
        self.StartGame.setGeometry(QtCore.QRect(100, 260, 93, 28))
        self.StartGame.setAutoDefault(False)
        self.StartGame.setFlat(False)
        self.StartGame.setObjectName("StartGame")
        self.Background = QtWidgets.QLabel(Form)
        self.Background.setGeometry(QtCore.QRect(0, 0, 301, 301))
        self.Background.setText("")
        self.Background.setPixmap(QtGui.QPixmap(":/image/1.jpg"))
        self.Background.setObjectName("Background")
        self.Background.raise_()
        self.StartGame.raise_()

        self.retranslateUi(Form)
        self.StartGame.clicked.connect(Form.show_message)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "好兄弟博饼"))
        Form.setToolTip(_translate("Form", "<html><head/><body><p align=\"center\">点击开始博饼</p></body></html>"))
        self.StartGame.setToolTip(_translate("Form", "<html><head/><body><p>点击开始博饼</p></body></html>"))
        self.StartGame.setText(_translate("Form", "开始游戏"))
import picture
