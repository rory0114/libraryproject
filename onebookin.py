# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '单本入库.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_bookin(object):
    def setupUi(self, bookin):
        bookin.setObjectName("bookin")
        bookin.resize(500, 600)
        self.label = QtWidgets.QLabel(bookin)
        self.label.setGeometry(QtCore.QRect(40, 40, 371, 41))
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(17)
        self.label.setFont(font)
        self.label.setAutoFillBackground(True)
        self.label.setObjectName("label")
        self.horizontalLayoutWidget = QtWidgets.QWidget(bookin)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(60, 100, 381, 291))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_2 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_2.setAutoFillBackground(True)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.label_4 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_4.setObjectName("label_4")
        self.verticalLayout.addWidget(self.label_4)
        self.label_3 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        self.label_5 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_5.setObjectName("label_5")
        self.verticalLayout.addWidget(self.label_5)
        self.label_6 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_6.setObjectName("label_6")
        self.verticalLayout.addWidget(self.label_6)
        self.label_8 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_8.setObjectName("label_8")
        self.verticalLayout.addWidget(self.label_8)
        self.label_9 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_9.setObjectName("label_9")
        self.verticalLayout.addWidget(self.label_9)
        self.label_7 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_7.setObjectName("label_7")
        self.verticalLayout.addWidget(self.label_7)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.verticalLayout_2.addWidget(self.lineEdit_2)
        self.lineEdit = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        self.lineEdit.setObjectName("lineEdit")
        self.verticalLayout_2.addWidget(self.lineEdit)
        self.lineEdit_3 = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.verticalLayout_2.addWidget(self.lineEdit_3)
        self.lineEdit_4 = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.verticalLayout_2.addWidget(self.lineEdit_4)
        self.lineEdit_5 = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.verticalLayout_2.addWidget(self.lineEdit_5)
        self.lineEdit_7 = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.verticalLayout_2.addWidget(self.lineEdit_7)
        self.lineEdit_8 = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        self.lineEdit_8.setObjectName("lineEdit_8")
        self.verticalLayout_2.addWidget(self.lineEdit_8)
        self.lineEdit_6 = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.verticalLayout_2.addWidget(self.lineEdit_6)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.horizontalLayout.setStretch(0, 1)
        self.horizontalLayout.setStretch(1, 4)
        self.pushButton = QtWidgets.QPushButton(bookin)
        self.pushButton.setGeometry(QtCore.QRect(320, 460, 112, 34))
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(bookin)
        QtCore.QMetaObject.connectSlotsByName(bookin)

    def retranslateUi(self, bookin):
        _translate = QtCore.QCoreApplication.translate
        bookin.setWindowTitle(_translate("bookin", "Form"))
        self.label.setText(_translate("bookin", "请登记入库图书"))
        self.label_2.setText(_translate("bookin", "书号"))
        self.label_4.setText(_translate("bookin", "类别"))
        self.label_3.setText(_translate("bookin", "书名"))
        self.label_5.setText(_translate("bookin", "出版社"))
        self.label_6.setText(_translate("bookin", "年份"))
        self.label_8.setText(_translate("bookin", "作者"))
        self.label_9.setText(_translate("bookin", "价格"))
        self.label_7.setText(_translate("bookin", "数量"))
        self.pushButton.setText(_translate("bookin", "单本入库"))

