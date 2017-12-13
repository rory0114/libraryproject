# -*- coding: utf-8 -*-
"""
Created on Fri Dec  8 20:51:55 2017

@author: lyr
"""
from PyQt5 import QtCore, QtGui, QtWidgets
from returnbook import Ui_Form
import pymysql
import datetime
import globalval

class retbook(QtWidgets.QWidget, Ui_Form):
    def __init__(self, parent=None):
        super(retbook, self).__init__(parent)
        self.setupUi(self)
        self.pushButton.clicked.connect(self.retconfirm)



#还书确认
    def retconfirm(self):
        idb = self.lineEdit.text()
        idc = self.lineEdit_2.text()
        try:
            db = pymysql.connect("localhost","root","","library",charset='utf8' )
            cursor = db.cursor()
            sql = """update  record set retday="%s" where 
                    idb='%s' and idc='%s' """%(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'),idb,idc)
            print(sql)
            sql="""update book set remain=remain+1 where idb='%s' and remain<number"""%(idb)
            cursor.execute(sql)
            db.commit()
        
            db.close()
            QtWidgets.QMessageBox.information(self,"Information","还书成功")
        except:
             QtWidgets.QMessageBox.information(self,"Information","还书失败")
            
        
