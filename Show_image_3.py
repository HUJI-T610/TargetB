# useful links :
# https://stackoverflow.com/questions/15204470/pyqt-how-to-get-a-widgets-dimensions
# https://stackoverflow.com/questions/43126721/detect-resizing-in-widget-window-resized-signal
#
import sys
from PyQt5.QtCore import Qt, QPoint
from PyQt5.QtWidgets import QMainWindow, QApplication, QLabel
from PyQt5.QtGui import QPixmap, QPainter, QPen

from PyQt5.QtWidgets import QApplication, QWidget, QLabel
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5 import QtWidgets

import numpy as np

'''
This class is a window where the marks on the image are made.
'''
class Window_image_draw(QMainWindow):
    def __init__(self, path, three_point_CT):
        #super(Window_image_draw, self).__init__()
        super().__init__()
        self.init_window()
        
        # labels :
        self.init_labels()
        
        # buttons :
        self.init_buttons()
        
        # Image :
        self.label_image = image_draw(path, three_point_CT, self.window_width, self.window_height, self)
        self.horizontalLayout_2.addWidget(self.label_image)
        
        # center the window :
        self.center_window()
        
        self.mesages_to_user = ["mark one side", "mark the disease", "mark the second side"]
        self.index_area = -1 # an index for divideing the data for 3 draw\parts .
    
    '''
    This function initialize the some parmeters of the window.
    '''
    def init_window(self):
        self.window_width = 656
        self.window_height = 251
        self.setGeometry(0, 0, self.window_width, self.window_height)
        self.setWindowTitle("Mark Image")
        
        self.widget = QWidget()
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.widget.setLayout(self.verticalLayout_2)
        self.setCentralWidget(self.widget)
    
    '''
    This function initialize the labels in the window.
    '''
    def init_labels(self):
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.labelA = QtWidgets.QLabel(self.widget)
        self.labelA.setText('only when you press the \'Next\' button you\nsave the part that you draw to represent it.')
        self.verticalLayout_3.addWidget(self.labelA)
        
        self.labelB = QtWidgets.QLabel(self.widget)
        self.labelB.setText('To start press \'Next\' button')
        self.verticalLayout_3.addWidget(self.labelB)
    
    '''
    This function initialize the buttons in the window.
    '''
    def init_buttons(self):
        self.pushButton = QtWidgets.QPushButton(self.widget)
        self.pushButton.setObjectName("pushButton")
        self.pushButton.setText('Next')
        self.verticalLayout_3.addWidget(self.pushButton)
        self.pushButton.clicked.connect(self.next_draw)
        
        self.horizontalLayout_2.addLayout(self.verticalLayout_3)
    
    '''
    Make the window apper at the center of the user screan.
    '''    
    def center_window(self):
        qtRectangle = self.frameGeometry()
        centerPoint = QtWidgets.QDesktopWidget().availableGeometry().center()
        qtRectangle.moveCenter(centerPoint)
        self.move(qtRectangle.topLeft())
       
    '''
    This function comtrols in which group of points each point is draw; side1, 
    diasse, side2.
    '''
    def next_draw(self):
        if (self.index_area == 2):
            self.close()
        else:
            self.index_area += 1
            self.labelB.setText(self.mesages_to_user[self.index_area])
        
        if (self.index_area == 2):
            self.pushButton.setText('finish')
    
    '''
    A getter function, returns a pointer to the image label.
    '''        
    def get_image_label(self):
        return self.label_image

'''
This class is a label with some functions added in order to ba able to draw
on the image.
'''
class image_draw(QLabel):
    def __init__(self, path, three_point_CT, window_width, window_height, parent=None):
        super(image_draw, self).__init__(parent.widget)
        self.window_width = window_width
        self.window_height = window_height
        self.drawing = False
        self.lastPoint = QPoint()
        self.image = QPixmap(path)
        self.setGeometry(100, 100, 500, 800)
        self.resize(self.image.width(), self.image.height())
        
        self.parent = parent 
        self.temp_data_area = []
        self.three_point_CT = three_point_CT
        

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.drawPixmap(self.rect(), self.image)

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.drawing = True
            self.lastPoint = event.pos()
            #start
      
    def mouseMoveEvent(self, event):
        if event.buttons() and Qt.LeftButton and self.drawing:
            # upadte the point to Stretch or Collapse of the image :
            point_pos = self.update_point_new_image_size(event.pos())
            point_last = self.update_point_new_image_size(self.lastPoint)
            
            painter = QPainter(self.image)
            painter.setPen(QPen(Qt.red, 3, Qt.SolidLine))
            painter.drawLine(point_last, point_pos)
            self.lastPoint = event.pos()
            
            self.temp_data_area.append([point_pos.x(), point_pos.y()])            
            self.update()
        

    def mouseReleaseEvent(self, event):
        #paused
        self.three_point_CT[self.parent.index_area-1].extend(self.temp_data_area)
        self.temp_data_area = []
        # TODO: control here the via "self.parent" the label to update the instractions
        if event.button == Qt.LeftButton:
            self.drawing = False


    def update_point_new_image_size(self, point):
        # We divide the self.window_width by two because we divided the window to 2 parts/ labels.
        self.dw = self.image.width() / (self.window_width / 2)
        self.dh = self.image.height() / self.window_height 
        return QPoint(point.x() * self.dw, point.y() * self.dh)
    
    # Detect resize of the window
    def resizeEvent(self, event):
        # We multiply by 2 because later we divied by 2.
        self.window_width = self.frameGeometry().width() * 2
        self.window_height = self.frameGeometry().height()
        print("someFunction")
        return super(image_draw, self).resizeEvent(event)
    
    def get_image(self):
        return self.image
        
'''
This class is a simple window that shows olny an image label.
'''
class Window_image(QMainWindow):
    def __init__(self, image_label, point1, point2):
        super().__init__()
        self.point1 = point1
        self.point2 = point2
        self.image_label = image_label
        
        self.initUI()
        
        # center the window :
        self.center_window()
    
    '''
    Make the window apper at the center of the user screan.
    '''  
    def center_window(self):
        qtRectangle = self.frameGeometry()
        centerPoint = QtWidgets.QDesktopWidget().availableGeometry().center()
        qtRectangle.moveCenter(centerPoint)
        self.move(qtRectangle.topLeft())
    
    '''
    This function initialize the some parmeters of the window.
    '''
    def initUI(self):
        self.title = 'Processed image'
        self.left = 10
        self.top = 10
        self.width = 640
        self.height = 480
        
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
    
        # Create widget
        label = QLabel(self)
        self.resize(self.image_label.get_image().width(),self.image_label.get_image().height())
        self.setCentralWidget(label)
    
    '''
    This function draw the line ("axis") where the electromagnets need to be
    at the side of this line.
    '''
    def paintEvent(self, event):
        super(Window_image, self).paintEvent(event)
        painter = QPainter()
        painter.begin(self)
        painter.setRenderHint(QPainter.Antialiasing)
        painter.drawPixmap(self.rect(), self.image_label.get_image())
        painter.setPen(QPen(Qt.blue, 4, Qt.SolidLine))
        painter.setBrush(Qt.white)
        painter.drawLine(self.point1[0][0], self.point1[1][0], self.point2[0][0], self.point2[1][0])
    

