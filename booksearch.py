# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '图书查询.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_booksearch(object):
    def setupUi(self, booksearch):
        booksearch.setObjectName("booksearch")
        booksearch.resize(1000, 600)
        self.tableWidget = QtWidgets.QTableWidget(booksearch)
        self.tableWidget.setGeometry(QtCore.QRect(60, 150, 891, 401))
        self.tableWidget.setAutoScrollMargin(15)
        self.tableWidget.setDragEnabled(True)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(9)
        self.tableWidget.setRowCount(10)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(9, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(8, item)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(98)
        self.tableWidget.verticalHeader().setDefaultSectionSize(33)
        self.query_label = QtWidgets.QLabel(booksearch)
        self.query_label.setGeometry(QtCore.QRect(50, 30, 231, 41))
        font = QtGui.QFont()
        font.setPointSize(17)
        self.query_label.setFont(font)
        self.query_label.setObjectName("query_label")
        self.horizontalLayoutWidget = QtWidgets.QWidget(booksearch)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(60, 70, 841, 61))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.h1 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.h1.setContentsMargins(0, 0, 0, 0)
        self.h1.setObjectName("h1")
        self.h1v4 = QtWidgets.QVBoxLayout()
        self.h1v4.setObjectName("h1v4")
        self.h1v4label1 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.h1v4label1.setObjectName("h1v4label1")
        self.h1v4.addWidget(self.h1v4label1)
        self.h1v4line1 = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        self.h1v4line1.setObjectName("h1v4line1")
        self.h1v4.addWidget(self.h1v4line1)
        self.h1.addLayout(self.h1v4)
        self.h1v5 = QtWidgets.QVBoxLayout()
        self.h1v5.setObjectName("h1v5")
        self.h1v5label1 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.h1v5label1.setObjectName("h1v5label1")
        self.h1v5.addWidget(self.h1v5label1)
        self.h1v5line1 = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        self.h1v5line1.setObjectName("h1v5line1")
        self.h1v5.addWidget(self.h1v5line1)
        self.h1.addLayout(self.h1v5)
        self.h1v6 = QtWidgets.QVBoxLayout()
        self.h1v6.setObjectName("h1v6")
        self.h1v6label1 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.h1v6label1.setObjectName("h1v6label1")
        self.h1v6.addWidget(self.h1v6label1)
        self.h1v6line1 = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        self.h1v6line1.setObjectName("h1v6line1")
        self.h1v6.addWidget(self.h1v6line1)
        self.h1.addLayout(self.h1v6)
        self.h1v3 = QtWidgets.QVBoxLayout()
        self.h1v3.setObjectName("h1v3")
        self.h1v3label1 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.h1v3label1.setObjectName("h1v3label1")
        self.h1v3.addWidget(self.h1v3label1)
        self.h1v3line1 = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        self.h1v3line1.setObjectName("h1v3line1")
        self.h1v3.addWidget(self.h1v3line1)
        self.h1.addLayout(self.h1v3)
        self.h1v2 = QtWidgets.QVBoxLayout()
        self.h1v2.setObjectName("h1v2")
        self.h1v2label1 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.h1v2label1.setObjectName("h1v2label1")
        self.h1v2.addWidget(self.h1v2label1)
        self.h1v2h1 = QtWidgets.QHBoxLayout()
        self.h1v2h1.setObjectName("h1v2h1")
        self.h1v2h1line2 = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        self.h1v2h1line2.setObjectName("h1v2h1line2")
        self.h1v2h1.addWidget(self.h1v2h1line2)
        self.h1v2h1label1 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.h1v2h1label1.setObjectName("h1v2h1label1")
        self.h1v2h1.addWidget(self.h1v2h1label1)
        self.h1v2h1line1 = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        self.h1v2h1line1.setObjectName("h1v2h1line1")
        self.h1v2h1.addWidget(self.h1v2h1line1)
        self.h1v2.addLayout(self.h1v2h1)
        self.h1.addLayout(self.h1v2)
        self.h1v1 = QtWidgets.QVBoxLayout()
        self.h1v1.setObjectName("h1v1")
        self.h1v1label1 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.h1v1label1.setObjectName("h1v1label1")
        self.h1v1.addWidget(self.h1v1label1)
        self.h1v1line1 = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        self.h1v1line1.setObjectName("h1v1line1")
        self.h1v1.addWidget(self.h1v1line1)
        self.h1.addLayout(self.h1v1)
        self.h1.setStretch(0, 10)
        self.h1.setStretch(1, 20)
        self.h1.setStretch(2, 20)
        self.h1.setStretch(3, 10)
        self.h1.setStretch(4, 20)
        self.h1.setStretch(5, 10)
        self.pushButton = QtWidgets.QPushButton(booksearch)
        self.pushButton.setGeometry(QtCore.QRect(910, 80, 51, 51))
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(booksearch)
        QtCore.QMetaObject.connectSlotsByName(booksearch)

    def retranslateUi(self, booksearch):
        _translate = QtCore.QCoreApplication.translate
        booksearch.setWindowTitle(_translate("booksearch", "Form"))
        item = self.tableWidget.verticalHeaderItem(0)
        item.setText(_translate("booksearch", "1"))
        item = self.tableWidget.verticalHeaderItem(1)
        item.setText(_translate("booksearch", "2"))
        item = self.tableWidget.verticalHeaderItem(2)
        item.setText(_translate("booksearch", "3"))
        item = self.tableWidget.verticalHeaderItem(3)
        item.setText(_translate("booksearch", "4"))
        item = self.tableWidget.verticalHeaderItem(4)
        item.setText(_translate("booksearch", "5"))
        item = self.tableWidget.verticalHeaderItem(5)
        item.setText(_translate("booksearch", "6"))
        item = self.tableWidget.verticalHeaderItem(6)
        item.setText(_translate("booksearch", "7"))
        item = self.tableWidget.verticalHeaderItem(7)
        item.setText(_translate("booksearch", "8"))
        item = self.tableWidget.verticalHeaderItem(8)
        item.setText(_translate("booksearch", "9"))
        item = self.tableWidget.verticalHeaderItem(9)
        item.setText(_translate("booksearch", "10"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("booksearch", "书号"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("booksearch", "类别"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("booksearch", "书名"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("booksearch", "出版社"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("booksearch", "年份"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("booksearch", "作者"))
        item = self.tableWidget.horizontalHeaderItem(6)
        item.setText(_translate("booksearch", "价格"))
        item = self.tableWidget.horizontalHeaderItem(7)
        item.setText(_translate("booksearch", "总藏书量"))
        item = self.tableWidget.horizontalHeaderItem(8)
        item.setText(_translate("booksearch", "库存"))
        self.query_label.setText(_translate("booksearch", "查询"))
        self.h1v4label1.setText(_translate("booksearch", "类别"))
        self.h1v5label1.setText(_translate("booksearch", "书名"))
        self.h1v6label1.setText(_translate("booksearch", "出版社"))
        self.h1v3label1.setText(_translate("booksearch", "年份"))
        self.h1v2label1.setText(_translate("booksearch", "价格"))
        self.h1v2h1label1.setText(_translate("booksearch", "至"))
        self.h1v1label1.setText(_translate("booksearch", "作者"))
        self.pushButton.setText(_translate("booksearch", "查找"))

