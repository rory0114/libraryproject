# -*- coding: utf-8 -*-
"""
Created on Fri Dec  8 20:45:35 2017

@author: lyr
"""

from PyQt5 import QtCore, QtGui, QtWidgets
from lend import Ui_lend
class lend(QtWidgets.QWidget, Ui_lend):
    def __init__(self, parent=None):
        super(lend, self).__init__(parent)
        self.setupUi(self)