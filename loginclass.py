# -*- coding: utf-8 -*-
"""
Created on Fri Dec  8 20:54:39 2017

@author: lyr
"""

from PyQt5 import QtCore, QtGui, QtWidgets
from login import Ui_Form
import pymysql
import globalval

class login(QtWidgets.QWidget, Ui_Form):
    def __init__(self, parent=None):
        super(login, self).__init__(parent)
        self.setupUi(self)
        
        #self.buttonBox.Ok.clicked.connect(self.varify)
        #self.buttonBox.Cancel.clicked.connect()

    #验证账号密码
    def varify(self):
        name=self.lineEdit_2.text()
        passw=self.lineEdit.text()
        db = pymysql.connect("localhost","root","","library",charset='utf8' )
        cursor = db.cursor()
        sql = """select * from librarian
                where idm='%s' and pw='%s'"""%(name,passw)
        print(sql)
        cursor.execute(sql) 
        result = cursor.fetchone()
        if result is not None:
            globval.setval(result[0])
            
        else:
            QtWidgets.QMessageBox.information(self,"Information","管理员登录失败，请重试")
            
        db.close()

        
