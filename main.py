# -*- coding: utf-8 -*-
"""
Created on Fri Dec  8 19:32:02 2017

@author: lyr
"""
from PyQt5 import QtCore, QtGui, QtWidgets
from homepageclass import  homepage
import sys
from booksearchclass import booksearch

if __name__=="__main__":
    app = QtWidgets.QApplication(sys.argv)
    global homepage
    global booksearch
    homepage=homepage()
    homepage.show()
  
    
    print("1")
    sys.exit(app.exec_())
    
