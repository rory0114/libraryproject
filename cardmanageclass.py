# -*- coding: utf-8 -*-
"""
Created on Fri Dec  8 20:38:52 2017

@author: lyr
"""

from PyQt5 import QtCore, QtGui, QtWidgets
from cardmanage import Ui_card_manage
import pymysql

class cardmanage(QtWidgets.QWidget, Ui_card_manage):
    def __init__(self, parent=None):
        super(cardmanage, self).__init__(parent)
        self.setupUi(self)
        self.pushButton_2.clicked.connect(self.addcard)

        self.pushButton.clicked.connect(self.delcard)

#添加借书证
    def addcard(self):
        idc=self.lineEdit_2.text()
        cname=self.lineEdit_3.text()
        company=self.lineEdit.text()
        cclass=self.comboBox.currentText()
        
        try:
            db = pymysql.connect("localhost","root","","library",charset='utf8' )
            cursor = db.cursor()
            sql = """INSERT INTO card(idc,cname,company,cclass)
             VALUES ('%s', '%s', '%s','%s')"""%(idc,cname,company,cclass)
            print(sql)
            cursor.execute(sql)
            db.commit()
            db.close()
            QtWidgets.QMessageBox.information(self,"Information","添加成功")
        
        except:
            QtWidgets.QMessageBox.information(self,"Information","添加失败")


#删除借书证
    def delcard(self):
        idc=self.lineEdit_4.text()
        try:
            db = pymysql.connect("localhost","root","","library",charset='utf8' )
            cursor = db.cursor()
            sql = """delete from card
             where idc='%s' """%(idc)
            print(sql)
            cursor.execute(sql)
            db.commit()
            db.close()
            QtWidgets.QMessageBox.information(self,"Information","删除成功")
        except:
            QtWidgets.QMessageBox.information(self,"Information","删除失败")

        
        
