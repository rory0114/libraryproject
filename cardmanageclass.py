# -*- coding: utf-8 -*-
"""
Created on Fri Dec  8 20:38:52 2017

@author: lyr
"""

from PyQt5 import QtCore, QtGui, QtWidgets
from cardmanage import Ui_card_manage
class cardmanage(QtWidgets.QWidget, Ui_card_manage):
    def __init__(self, parent=None):
        super(cardmanage, self).__init__(parent)
        self.setupUi(self)
