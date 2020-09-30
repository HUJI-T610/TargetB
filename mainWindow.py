# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainWindow.ui'
# Created by: PyQt5 UI code generator 5.13.0
# From HUJI Project, by Raphael Haehnel, David Telepnev

# 0.0000000000000005

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *

from points import Points
from data_types import Electromagnet, Data
from calc_B import Calc_B
from Show_image_3 import Window_image_draw, Window_image
from DrawToPoints import draws_to_points
from arduino_control import arduino_control_window#arduino_control
from parameters_Settings import Parameters_Settings

import numpy as np
import sys
import threading


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(657, 314)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(657, 314))
        MainWindow.setMaximumSize(QtCore.QSize(657, 314))
        MainWindow.setMouseTracking(False)
        MainWindow.setAcceptDrops(True)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("res/favicon.gif"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon.addPixmap(QtGui.QPixmap("res/favicon.gif"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        MainWindow.setWindowIcon(icon)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setDockNestingEnabled(False)
        MainWindow.setDockOptions(QtWidgets.QMainWindow.AllowTabbedDocks|QtWidgets.QMainWindow.AnimatedDocks)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setObjectName("centralwidget")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(0, 10, 656, 251))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        spacerItem = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.pushButton = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout_4.addWidget(self.pushButton)
        self.pushButton_2 = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_2.setObjectName("pushButton_2")
        self.verticalLayout_4.addWidget(self.pushButton_2)
        self.pushButton_3 = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_3.setObjectName("pushButton_3")
        self.verticalLayout_4.addWidget(self.pushButton_3)
        self.horizontalLayout_6.addLayout(self.verticalLayout_4)
        spacerItem1 = QtWidgets.QSpacerItem(70, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem1)
        self.line = QtWidgets.QFrame(self.layoutWidget)
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.horizontalLayout_6.addWidget(self.line)
        spacerItem2 = QtWidgets.QSpacerItem(70, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem2)
        self.verticalLayout_7 = QtWidgets.QVBoxLayout()
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.pushButton_4 = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_4.setObjectName("pushButton_4")
        self.verticalLayout_7.addWidget(self.pushButton_4)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.label_4 = QtWidgets.QLabel(self.layoutWidget)
        self.label_4.setText("")
        self.label_4.setPixmap(QtGui.QPixmap("res/magnet_left.png"))
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_5.addWidget(self.label_4)
        self.label_5 = QtWidgets.QLabel(self.layoutWidget)
        self.label_5.setFrameShape(QtWidgets.QFrame.Box)
        self.label_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_5.addWidget(self.label_5)
        self.horizontalLayout_5.addLayout(self.verticalLayout_5)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem3)
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.label_3 = QtWidgets.QLabel(self.layoutWidget)
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap("res/magnet_right.png"))
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_6.addWidget(self.label_3)
        self.label_6 = QtWidgets.QLabel(self.layoutWidget)
        self.label_6.setFrameShape(QtWidgets.QFrame.Box)
        self.label_6.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.verticalLayout_6.addWidget(self.label_6)
        self.horizontalLayout_5.addLayout(self.verticalLayout_6)
        self.verticalLayout_7.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_6.addLayout(self.verticalLayout_7)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem4)
        self.verticalLayout_8.addLayout(self.horizontalLayout_6)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.groupBox = QtWidgets.QGroupBox(self.layoutWidget)
        self.groupBox.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy)
        self.groupBox.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.groupBox.setFlat(False)
        self.groupBox.setCheckable(False)
        self.groupBox.setObjectName("groupBox")
        self.layoutWidget1 = QtWidgets.QWidget(self.groupBox)
        self.layoutWidget1.setGeometry(QtCore.QRect(10, 40, 291, 61))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.layoutWidget1)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label = QtWidgets.QLabel(self.layoutWidget1)
        self.label.setObjectName("label")
        self.horizontalLayout_3.addWidget(self.label)
        self.checkBox = QtWidgets.QCheckBox(self.layoutWidget1)
        self.checkBox.setText("")
        self.checkBox.setObjectName("checkBox")
        self.horizontalLayout_3.addWidget(self.checkBox)
        self.lineEdit = QtWidgets.QLineEdit(self.layoutWidget1)
        self.lineEdit.setEnabled(False)
        self.lineEdit.setObjectName("line")
        self.horizontalLayout_3.addWidget(self.lineEdit)
        self.verticalLayout_3.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_2 = QtWidgets.QLabel(self.layoutWidget1)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_4.addWidget(self.label_2)
        self.checkBox_2 = QtWidgets.QCheckBox(self.layoutWidget1)
        self.checkBox_2.setText("")
        self.checkBox_2.setObjectName("checkBox_2")
        self.horizontalLayout_4.addWidget(self.checkBox_2)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.layoutWidget1)
        self.lineEdit_2.setEnabled(False)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.horizontalLayout_4.addWidget(self.lineEdit_2)
        self.verticalLayout_3.addLayout(self.horizontalLayout_4)
        self.label_7 = QtWidgets.QLabel(self.groupBox)
        self.label_7.setGeometry(QtCore.QRect(430, 40, 211, 51))
        self.label_7.setText("")
        self.label_7.setPixmap(QtGui.QPixmap("res/logo_huji.png"))
        self.label_7.setScaledContents(True)
        self.label_7.setObjectName("label_7")
        self.verticalLayout_2.addWidget(self.groupBox)
        self.verticalLayout_8.addLayout(self.verticalLayout_2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 657, 26))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuSettings = QtWidgets.QMenu(self.menubar)
        self.menuSettings.setObjectName("menuSettings")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionNew = QtWidgets.QAction(MainWindow)
        self.actionNew.setObjectName("actionNew")
        self.actionOpen = QtWidgets.QAction(MainWindow)
        self.actionOpen.setObjectName("actionOpen")
        self.actionQuit = QtWidgets.QAction(MainWindow)
        self.actionQuit.setObjectName("actionQuit")
        self.actionUpload = QtWidgets.QAction(MainWindow)
        self.actionUpload.setObjectName("actionUpload")
        self.actionParameters = QtWidgets.QAction(MainWindow)
        self.actionParameters.setObjectName("actionParameters")
        self.actionAbout = QtWidgets.QAction(MainWindow)
        self.actionAbout.setObjectName("actionAbout")
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionNew)
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addAction(self.actionQuit)
        self.menuSettings.addAction(self.actionUpload)
        self.menuSettings.addAction(self.actionParameters)
        self.menuHelp.addAction(self.actionAbout)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuSettings.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)
        self.checkBox.toggled['bool'].connect(self.lineEdit.setEnabled)
        self.checkBox_2.toggled['bool'].connect(self.lineEdit_2.setEnabled)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        # Connect the menu bar to slots
        self.connectMenubar()

        # Connect the buttons to slots
        self.connectButtons()
        
        # Functinality parameters and not GUI
        self.set_functinality_parameters()
        
    def set_functinality_parameters(self):
        self.three_point_CT = [[], [], []]
        self.file_path = None
        self.time_oscillate = 0.5
        self.flag_uploaded_image = False
        self.current_adruino_1 = 0
        self.current_adruino_2 = 0
        self.data_parmeters = Data() # defult settings and values
        self.electromagnet_parameters = self.data_parmeters.get_electromagnet()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "TargetB"))
        self.pushButton.setText(_translate("MainWindow", "Upload Image"))
        self.pushButton_2.setText(_translate("MainWindow", "Redefine points"))
        self.pushButton_3.setText(_translate("MainWindow", "Display Image"))
        self.pushButton_4.setText(_translate("MainWindow", "COMPUTE"))
        self.label_5.setText(_translate("MainWindow", "I = 0A"))
        self.label_6.setText(_translate("MainWindow", "I = 0A"))
        self.groupBox.setTitle(_translate("MainWindow", "Options"))
        self.label.setText(_translate("MainWindow", "Magnetic field"))
        self.label_2.setText(_translate("MainWindow", "Time constant"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuSettings.setTitle(_translate("MainWindow", "Settings"))
        self.menuHelp.setTitle(_translate("MainWindow", "Help"))
        self.actionNew.setText(_translate("MainWindow", "New"))
        self.actionOpen.setText(_translate("MainWindow", "Open"))
        self.actionQuit.setText(_translate("MainWindow", "Quit"))
        self.actionUpload.setText(_translate("MainWindow", "Upload"))
        self.actionParameters.setText(_translate("MainWindow", "Parameters"))
        self.actionAbout.setText(_translate("MainWindow", "About"))

    def connectMenubar(self):
        self.actionAbout.triggered.connect(self.show_about_dialog)
        self.actionNew.triggered.connect(self.slot_New)
        self.actionOpen.triggered.connect(self.slot_Open)
        self.actionQuit.triggered.connect(MainWindow.close)
        self.actionUpload.triggered.connect(self.slot_Upload)
        self.actionParameters.triggered.connect(self.slot_Parameters)

    def connectButtons(self):
        self.pushButton.clicked.connect(self.slot_UploadImage)
        self.pushButton_2.clicked.connect(self.slot_RedefinePoints)
        self.pushButton_3.clicked.connect(self.slot_DisplayPoints)
        self.pushButton_4.clicked.connect(self.slot_Compute)

    def slot_Upload(self):
        self.window_arduino = arduino_control_window(self.time_oscillate, self.current_adruino_1, self.current_adruino_2)
        thread = threading.Thread(target=self.window_arduino.show())
    
    def slot_Parameters(self):
        self.parameters_settings_class = Parameters_Settings(self.data_parmeters)
        self.parameters_settings_class.show()

    def slot_New(self):
        """
        Slot connected to the action "New".
        :return: none
        """
        pass

    def slot_Open(self):
        """
        Slot connected to the action "Open".
        :return: none
        """
        path = self.open_file()
        if path:
            # print("Open file is here , code ctrl+F: 123444")
            # pass
            self.flag_uploaded_image = True

    def slot_UploadImage(self):
        """
        Slot connected to the button "Upload Image".
        :return: none
        """
        path = self.open_file()
        if path:
            self.flag_uploaded_image = True

    def slot_RedefinePoints(self):
        """
        Slot connected to the button "Redefine Points".
        :return: none
        """
        if(self.flag_uploaded_image):
            self.w = Window_image_draw(self.file_path, self.three_point_CT)
            self.w.show()

            # We need to upload a new image if we want to mark an image.
            self.flag_uploaded_image = False
        else:
            # pop-up window
            msg = QMessageBox()
            msg.setWindowTitle("Computing")
            msg.setIcon(QMessageBox.Critical)
            msg.setText("No image") # with marks
            x = msg.exec_()

    def slot_DisplayPoints(self):
        """
        Slot connected to the button "Display Points".
        :return: none
        """
        try:
            self.dtp = draws_to_points(self.three_point_CT)
            self.points_from_image = self.dtp.get_points_from_image()
            points = self.points_from_image
            point1 = points[0]
            point2 = points[1] 
            
            if (self.file_path != None):
                self.w2 = Window_image(self.w.get_image_label(), point1, point2)
                self.w2.show()
        except:
            # pop-up window
            msg = QMessageBox()
            msg.setWindowTitle("Computing")
            msg.setIcon(QMessageBox.Critical)
            msg.setText("No image") # with marks
            x = msg.exec_()

    def slot_Compute(self):
        """
        Slot connected to the button "Compute".
        :return: none
        """
        magnetic_field = self.lineEdit.text()
        time_constant = self.lineEdit_2.text()
        print(time_constant)
        
        try:
            magnetic_field = float(magnetic_field.split()[0])
        except:
            # Bad input, we will get minimum B for I = 1 A
            magnetic_field = 0
        
        try:
            time_constant = float(time_constant.split()[0])
        except:
            time_constant = 0.5
                  
        self.time_oscillate = time_constant
        
        try:
            points = self.points_from_image
            p1 = points[0]
            p2 = points[1]
            p3 = points[2]
            p4 = points[3]
            ratio = self.data_parmeters.get_ratio()
            all_points = Points(p1, p3, p2, p4, ratio)
            
            self.calculation_of_B = Calc_B(magnetic_field, all_points, self.electromagnet_parameters)
            self.calculation_of_B.calculate_B_and_I_coil1()
            self.calculation_of_B.calculate_B_and_I_coil2()
            
            self.current_adruino_1 = self.calculation_of_B.get_I_coil1()
            self.current_adruino_2 = self.calculation_of_B.get_I_coil2()
            
            _translate = QtCore.QCoreApplication.translate
            
            I1 = f'{self.current_adruino_1:.4f}'
            I2 = f'{self.current_adruino_2:.4f}'
            self.label_5.setText(_translate("MainWindow", "I = " + str(I1) + "A"))
            self.label_6.setText(_translate("MainWindow", "I = " + str(I2) + "A"))

        except:
            # pop-up window
            msg = QMessageBox()
            msg.setWindowTitle("Computing")
            msg.setIcon(QMessageBox.Critical)
            msg.setText("No image with marks")
            x = msg.exec_()

    def open_file(self):
        """
        This function is opening the file explorer and return the path of the chosen file
        :return: the file path
        """
        path = QFileDialog.getOpenFileName(MainWindow, "Open")[0]
        if path:
            self.file_path = path
        return path

    def save(self):
        """
        This function is opening the file explorer to save a file
        :return: none
        """
        if self.file_path is None:
            self.save_as()
        else:
            with open(self.file_path, "w") as f:
                pass

    def save_as(self):
        """
        This function is opening the file explorer to save a file by using the function save()
        :return: none
        """
        path = QFileDialog.getSaveFileName(MainWindow, "Save As")[0]
        if path:
            self.file_path = path
            self.save()

    def show_about_dialog(self):
        """
        Display the 'about' window
        :return: none
        """
        text = "<center>" \
               "<h1>TargetB</h1>" \
               "&#8291;" \
               "<img src=res/just_logo.png>" \
               "</center>" \
               "<p>Version 1.0<br/>" \
               "by Raphael Haehnel, David Telepnev<br/>" \
               "&copy; Hebrew University.</p>"
        QMessageBox.about(MainWindow, "About TargetB", text)


if __name__ == "__main__":
    print("started")
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
