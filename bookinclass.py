# -*- coding: utf-8 -*-
"""
Created on Fri Dec  8 20:50:02 2017

@author: lyr
"""

from PyQt5 import QtCore, QtGui, QtWidgets
from onebookin import Ui_bookin
import pymysql

class bookin(QtWidgets.QWidget, Ui_bookin):
    def __init__(self, parent=None):
        super(bookin, self).__init__(parent)
        self.setupUi(self)
        self.pushButton.clicked.connect(self.bookin)
    
    
    def bookin(self):
        idb = self.lineEdit_2.text()
        classb = self.lineEdit.text()
        bname = self.lineEdit_3.text()
        press = self.lineEdit_4.text()
        year = self.lineEdit_5.text()
        writer = self.lineEdit_7.text()
        price = self.lineEdit_8.text()
        number = self.lineEdit_6.text()

        db = pymysql.connect("localhost","root","","library",charset='utf8' )
        cursor = db.cursor()
        sql = """INSERT INTO book(idb,bclass,bname,press,year,writer,price,number,remain)
         VALUES ('%s', '%s', '%s','%s',%s,'%s', %s, %s,%s )"""%(idb,classb,bname,press,year,writer,price,number,number)
        print(sql)
        cursor.execute(sql)
        db.commit()
        db.close()
