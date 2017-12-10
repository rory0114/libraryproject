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