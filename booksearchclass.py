# -*- coding: utf-8 -*-
"""
Created on Fri Dec  8 20:02:56 2017

@author: lyr
"""

from PyQt5 import QtCore, QtGui, QtWidgets
from booksearch import Ui_booksearch
class booksearch(QtWidgets.QWidget, Ui_booksearch):
    def __init__(self, parent=None):
        super(booksearch, self).__init__(parent)
        self.setupUi(self)