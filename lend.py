# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'lend.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_lend(object):
    def setupUi(self, lend):
        lend.setObjectName("lend")
        lend.resize(500, 300)
        self.label = QtWidgets.QLabel(lend)
        self.label.setGeometry(QtCore.QRect(40, 20, 111, 41))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.verticalLayoutWidget = QtWidgets.QWidget(lend)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(60, 60, 381, 161))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_2 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.lineEdit = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout.addWidget(self.lineEdit)
        self.horizontalLayout.setStretch(0, 1)
        self.horizontalLayout.setStretch(1, 4)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_3 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_2.addWidget(self.label_3)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.horizontalLayout_2.addWidget(self.lineEdit_2)
        self.horizontalLayout_2.setStretch(0, 1)
        self.horizontalLayout_2.setStretch(1, 4)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.pushButton = QtWidgets.QPushButton(lend)
        self.pushButton.setGeometry(QtCore.QRect(350, 240, 112, 34))
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(lend)
        QtCore.QMetaObject.connectSlotsByName(lend)

    def retranslateUi(self, lend):
        _translate = QtCore.QCoreApplication.translate
        lend.setWindowTitle(_translate("lend", "Form"))
        self.label.setText(_translate("lend", "借书"))
        self.label_2.setText(_translate("lend", "书号"))
        self.label_3.setText(_translate("lend", "借书证号"))
        self.pushButton.setText(_translate("lend", "确认"))

