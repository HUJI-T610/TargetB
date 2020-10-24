# -*- coding: utf-8 -*-
"""
Created on Mon Sep 14 17:37:18 2020

@author: David Tal
"""

from PyQt5.QtWidgets import QMainWindow, QApplication, QLabel, QWidget, QMessageBox, QLineEdit
from PyQt5 import QtWidgets
from PyQt5 import QtCore

from data_types import Electromagnet


class Parameters_Settings(QMainWindow):
    def __init__(self, data_parmeters):
        super().__init__()
        # data :
        self.ratio_value = 0.5 / 500 # actual size in meters divided by number of pixels
        self.data_parmeters = data_parmeters
        self.Rad = data_parmeters.get_electromagnet().get_R()
        self.Rat = data_parmeters.get_ratio()
        self.n = data_parmeters.get_electromagnet().get_n()
        
        # init the window :
        self.init_window()
        
        # Right side, Buttons :
        self.init_right_side()
        
        # left side, label + data show
        self.init_left_side()
        
        # init in the center bottom :
        self.init_center()
        
        # center the window :
        self.center_window()
        
    '''
    This function initialize the some parmeters of the window.
    '''
    def init_window(self):
        self.window_width = 656 / 2
        self.window_height = 251 / 3
        self.setGeometry(0, 0, self.window_width, self.window_height)#(100, 100, 500, 300)
        self.setWindowTitle("update the parameters")
        
        self.widget = QWidget()
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.widget.setLayout(self.verticalLayout)
        self.setCentralWidget(self.widget)
    
    '''
    This function defines and initialize the right side of the window layout.
    '''
    def init_right_side(self):
        self.verticalLayout_left = QtWidgets.QVBoxLayout()
        
        self.label_radius = QtWidgets.QLabel(self.widget)
        self.label_radius.setText('Radius of electromagnet : ')
        self.verticalLayout_left.addWidget(self.label_radius)
        
        self.label_windings = QtWidgets.QLabel(self.widget)
        self.label_windings.setText('number of windings : ')
        self.verticalLayout_left.addWidget(self.label_windings)
        
        self.label_ratio = QtWidgets.QLabel(self.widget)
        self.label_ratio.setText('ratio image to distance : ')
        self.verticalLayout_left.addWidget(self.label_ratio)
        
        self.horizontalLayout.addLayout(self.verticalLayout_left)
    
    '''
    This function defines and initialize the left side of the window layout.
    '''
    def init_left_side(self):
        self.verticalLayout_right = QtWidgets.QVBoxLayout()
        
        self.edit_radius = QLineEdit(self.widget)
        self.verticalLayout_right.addWidget(self.edit_radius)
        self.edit_radius.setText(str(self.Rad)) # '0.04'
        
        self.edit_windings = QLineEdit(self.widget)
        self.verticalLayout_right.addWidget(self.edit_windings)
        self.edit_windings.setText(str(self.n)) # '180'
        
        self.edit_ratio = QLineEdit(self.widget)
        self.verticalLayout_right.addWidget(self.edit_ratio)
        self.edit_ratio.setText(str(self.Rat))
        
        self.horizontalLayout.addLayout(self.verticalLayout_right)
    
    '''
    This function defines and initialize the center of the window layout.
    '''
    def init_center(self):
        self.horizontalLayout2 = QtWidgets.QHBoxLayout()
        
        self.pushButton_1 = QtWidgets.QPushButton(self.widget)
        self.pushButton_1.setObjectName("pushButton_1")
        self.pushButton_1.setText('Update')
        self.horizontalLayout2.addWidget(self.pushButton_1)
        self.pushButton_1.clicked.connect(self.update_button)
        
        self.verticalLayout.addLayout(self.horizontalLayout2)
        
    '''
    Make the window apper at the center of the user screan.
    '''
    def center_window(self):
        qtRectangle = self.frameGeometry()
        centerPoint = QtWidgets.QDesktopWidget().availableGeometry().center()
        qtRectangle.moveCenter(centerPoint)
        self.move(qtRectangle.topLeft())
    
    '''
    In update the values of the parmeters by what the user input.
    '''
    def update_button(self):
        print(self.edit_radius.text(), self.edit_windings.text(), self.edit_ratio.text())
        self.data_parmeters.get_electromagnet().set_R(float(self.edit_radius.text()))
        self.data_parmeters.get_electromagnet().set_n(float(self.edit_windings.text()))
        self.data_parmeters.set_ratio(float(self.edit_ratio.text()))
    
