# -*- coding: utf-8 -*-
"""
Created on Fri Dec  8 19:39:01 2017

@author: lyr
"""

from PyQt5 import QtCore, QtGui, QtWidgets
from homepage import Ui_homepage
from booksearchclass import booksearch
from bookinclass import bookin
from cardmanageclass import cardmanage
from lendclass import lend
from loginclass import login
from retbookclass import retbook


class homepage(QtWidgets.QWidget, Ui_homepage):
    def __init__(self, parent=None):
        super(homepage, self).__init__(parent)
        self.setupUi(self)
        #定义子窗口
        self.booksearch =   booksearch()
        self.bookin     =   bookin()
        self.cardmanage =   cardmanage()
        self.retbook    =   retbook()
        self.login      =   login()
        self.lend       =   lend()
        #定义子窗口打开按钮函数
        self.book_search_btn.clicked.connect(self.booksearch.show)
        self.card_manage_btn.clicked.connect(self.cardmanage.show)
        self.one_book_in_btn.clicked.connect(self.bookin.show)
        self.lend_ben.clicked.connect(self.lend.show)
        self.return_btn.clicked.connect(self.retbook.show)
        self.login_btn.clicked.connect(self.login.show)


        #定义
   
       
