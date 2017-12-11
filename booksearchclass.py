# -*- coding: utf-8 -*-
"""
Created on Fri Dec  8 20:02:56 2017

@author: lyr
"""

from PyQt5 import QtCore, QtGui, QtWidgets
from booksearch import Ui_booksearch
import pymysql


class booksearch(QtWidgets.QWidget, Ui_booksearch):
    def __init__(self, parent=None):
        super(booksearch, self).__init__(parent)
        self.setupUi(self)

        self.pushButton.clicked.connect(self.search)

#搜索
    def search(self):
        bclass = self.h1v4line1.text()
        bname = self.h1v5line1.text()
        press = self.h1v6line1.text()
        year = self.h1v3line1.text()
        price_down = self.h1v2h1line2.text()
        price_up = self.h1v2h1line1.text()
        writer = self.h1v1line1.text()
        sql="""select * from book where """
        dic={"bclass":bclass,"bname":bname,"press":press,"year":year,"price_down":price_down,"price_up":price_up,"writer":writer}
        anum=0
        for i in dic:
            print(i)
            print(anum)
            if dic[i]!="":
                if anum!=0:
                    sql=sql+" and "
                if i=="price_down":
                    s="%s>%s"%(i,dic[i])
                    sql=sql+s
                elif i=="price_up":
                    s="%s<%s"%(i,dic[i])
                    sql=sql+s
                elif i=="year":
                    s="%s=%s"%(i,dic[i])
                    sql=sql+s
                else:
                    s="%s='%s'"%(i,dic[i])
                    sql=sql+s
                anum=anum+1

        db = pymysql.connect("localhost","root","","library",charset='utf8' )
        cursor = db.cursor()           
        print(sql)
        cursor.execute(sql)
        result = cursor.fetchall()
        print(result)
        
        if result is None:           
            QtWidgets.QMessageBox.information(self,"Information","未找到该书")
        else:
            anum=0
            bnum=0
            for a in result:              
                for b in a:
                    print(str(b))
                    new=QtWidgets.QTableWidgetItem(str(b))
                    self.tableWidget.setItem(anum,bnum,new)
                    bnum=bnum+1
                anum=anum+1
                bnum=0
                
                
                        
                        
                    
            
            
