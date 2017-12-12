# -*- coding: utf-8 -*-
"""
Created on Fri Dec  8 20:45:35 2017

@author: lyr
"""

from PyQt5 import QtCore, QtGui, QtWidgets
from lend import Ui_lend
import pymysql
import datetime
import glovalvar
class lend(QtWidgets.QWidget, Ui_lend):
    def __init__(self, parent=None):
        super(lend, self).__init__(parent)
        self.setupUi(self)
        self.pushButton.clicked.connect(self.lendconfirm)


    #借书确认
    def lendconfirm(self):
        idb=self.lineEdit.text()
        idc=self.lineEdit_2.text()
        db = pymysql.connect("localhost","root","","library",charset='utf8' )
        cursor = db.cursor()
        sql = """INSERT INTO record(idc,idb,lenddate,idm)
           VALUES ('%s', '%s','%s', '%s','%s')"""%(idb,idc,datetime.datetime.now().strftime('%Y-%m-%d'), globalvar.getval())
        print(sql)
        try:
            cursor.execute(sql)
            db.commit()
            QtWidgets.QMessageBox.information(self,"Information","借书成功")
        except:
            QtWidgets.QMessageBox.information(self,"Information","借书失败")
            
        db.close()
