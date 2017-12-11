# -*- coding: utf-8 -*-
"""
Created on Fri Dec  8 20:51:55 2017

@author: lyr
"""
from PyQt5 import QtCore, QtGui, QtWidgets
from returnbook import Ui_Form
class retbook(QtWidgets.QWidget, Ui_Form):
    def __init__(self, parent=None):
        super(retbook, self).__init__(parent)
        self.setupUi(self)
        self.pushButton.clicked.connect(self.retconfirm)



#还书确认
    def retconfirm(self):
        idb = self.lineEdit.text()
        idc = self.lineEdit_2.text()
        db = pymysql.connect("localhost","root","","library",charset='utf8' )
        cursor = db.cursor()
        sql = """delete from record where
                idb='%s' and idc='%s' """%(idb,idc)
        print(sql)
        cursor.execute(sql)
        db.commit()
        db.close()
        
