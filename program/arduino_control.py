#from pyfirmata import Arduino, util
from pyfirmata2 import Arduino, util
import serial.tools.list_ports
import time
import sys
import threading

from PyQt5.QtWidgets import QMainWindow, QApplication, QLabel, QWidget, QMessageBox
from PyQt5 import QtWidgets
from PyQt5 import QtCore


# https://www.youtube.com/watch?v=mYPNHoPwIJI
# https://pythonprogramming.net/progress-bar-pyqt-tutorial/


'''
This class is the GUI of the window where we control the arduino.
'''
class arduino_control_window(QMainWindow):
    def __init__(self, time_oscillate, current_adruino_1, current_adruino_2):
        super().__init__()

        print("started arduino_control_window ")
        # oscillation time of the electromagnets :
        self.time_oscillate = time_oscillate
        
        # currents for each electromagnet :
        self.current_adruino_1 = current_adruino_1
        self.current_adruino_2 = current_adruino_2
        
        # init the window :
        self.init_window()
        
        # Right side, Buttons :
        self.init_right_side()
        
        # left side, label + data show
        self.init_left_side()
        
        # set time stuff :
        self.init_time()
        
        # center the window :
        self.center_window()
        
        # thread for the board control (handy for the infinite loop inside it) :
        self.thread_board = None
        self.ac = None

        # flag to start and stop the borad 'loop' :
        self.flag_arduino_working = True
        
        self.flag_first_time_thread = True

        # a pointer to the board connection :
        self.board = None
       
        # init thread :
        #self.init_thread()
    

    '''
    This function initialize the parmeters for "arduino_control" class. Also this
    class inhreates Thread class and because of it, it has parmeters for a thread.
    ''' 
    def init_thread(self):
        threadID = 1
        name = "Thread-1"
        self.thread_board = arduino_control(threadID, name, self.time_oscillate, self.board,
                                            self.current_adruino_1, self.current_adruino_2)

    '''
    This function initialize the some parmeters of the window.
    '''
    def init_window(self):
        self.window_width = 656 / 2
        self.window_height = 251 / 3
        self.setGeometry(0, 0, self.window_width, self.window_height)#(100, 100, 500, 300)
        self.setWindowTitle("arduino control")
        
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
        self.pushButton_1 = QtWidgets.QPushButton(self.widget)
        self.pushButton_1.setObjectName("pushButton_1")
        self.pushButton_1.setText('Start')
        self.verticalLayout_left.addWidget(self.pushButton_1)
        self.pushButton_1.clicked.connect(self.start_arduino)
        
        self.pushButton_2 = QtWidgets.QPushButton(self.widget)
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.setText('Stop')
        self.verticalLayout_left.addWidget(self.pushButton_2)
        self.pushButton_2.clicked.connect(self.stop_arduino)
        
        self.horizontalLayout.addLayout(self.verticalLayout_left)
    
    '''
    This function defines and initialize the left side of the window layout.
    '''
    def init_left_side(self):
        self.verticalLayout_right = QtWidgets.QVBoxLayout()
        self.label_time_count = QtWidgets.QLabel(self.widget)
        self.label_time_count.setText('Time : 00:00:00')
        self.verticalLayout_right.addWidget(self.label_time_count)
    
        
        self.horizontalLayout.addLayout(self.verticalLayout_right)
    
    '''
    This function initialze the parametrs of time/stopper/counter.
    '''
    def init_time(self): 
        self.timer = QtCore.QTimer()
        self.time = QtCore.QTime(0, 0, 0)
        self.timer.timeout.connect(self.timer_event)
        
        #self.timer.start(1000)
    
    '''
    Make the window apper at the center of the user screan.
    '''
    def center_window(self):
        qtRectangle = self.frameGeometry()
        centerPoint = QtWidgets.QDesktopWidget().availableGeometry().center()
        qtRectangle.moveCenter(centerPoint)
        self.move(qtRectangle.topLeft())
    
    '''
    This function statrts counter of time and send a 'start' command to the 
    arduino.
    '''
    def start_arduino(self):
        try:
            try:
                self.thread_board.exit()
            except:
                pass
            self.init_thread()
            self.timer.start(1000)
            self.thread_board.start()
        except:
            pass
    
    '''
    This function stops counter of time and send a 'stop' command to the 
    arduino.
    '''
    def stop_arduino(self):
        self.timer.stop()
        try:
            self.thread_board.exit2()
        except:
            pass
    
    '''
    Update the time and the time layout.
    '''
    def timer_event(self):
        self.time = self.time.addSecs(1)
        self.label_time_count.setText('Time : '+ self.time.toString("hh:mm:ss"))
        
        
    # '''
    # Some basic checking that we use the right port of communication with the
    # arduino.
    # '''
    # def check_ports(self):
    #     myports = [tuple(p) for p in list(serial.tools.list_ports.comports())]
    #     number_of_ports = len(myports)
        
    #     msg = QMessageBox()
    #     msg.setWindowTitle("arduino control")
    #     msg.setIcon(QMessageBox.Critical)
        
    #     if number_of_ports == 0:
    #         # pop up window - no port port found
    #         msg.setText("no port port found")
    #         x = msg.exec_()
    #         return False
    #     elif number_of_ports >= 2:
    #         # pop up window - please unplug and plug again the device
    #         msg.setText("please unplug and plug again the device")
    #         x = msg.exec_()
    #         return False
    #     else:
    #         return True
    
    # def closeEvent(self, event):
    #     print("Close arduino window")
    #     try:
    #         print("1",self.thread_board)
    #         self.board.exit()
    #         self.thread_board.exit()
    #         print("2",self.thread_board)
    #     except:
    #         pass
    #     #event.ignore()


'''
Via this class we control the arduino. 
'''
class arduino_control(threading.Thread): 
    def __init__(self, threadID, name, time_oscillate, external_pointer_board,
                 current_adruino_1, current_adruino_2):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        
        self.current_adruino_1 = current_adruino_1
        self.current_adruino_2 = current_adruino_2

        self.flag_arduino_working = True
        self.time_oscillate = time_oscillate
        self.init_arduino()

        self.external_pointer_board = external_pointer_board
        print(self.current_adruino_1, self.current_adruino_2, self.current_adruino_2/ 5.0)
        
        # voltages and currents arduino :
        # [ 0.15007188 -0.02560927] [ 0.1796672 -0.0954898]
        max_voltage = 5.0 # Volt
        # ratio between gate voltage to current by expereiment. average of both electroagnets :
        slope_electromagnet = (0.15007188 + 0.1796672) / 2 
        # this is the the 'b' in the 'y=a*x+b' :
        # bais_electromagnet = -(0.02560927 + 0.0954898) / 2 
        self.voltage_on_gate_1 = (self.current_adruino_1 / max_voltage) 
        self.voltage_on_gate_2 = (self.current_adruino_2 / max_voltage)
        
        
    '''
    This function is implements the oscillations, that is the frequency of 
    the oscillations.
    pin1 = the pin the we conent to electromagnet 1.
    pin2 = the pin the we conent to electromagnet 2.
    '''
    def oscillate(self, pin1, pin2):
        print("oscillate 1")
        time.sleep(self.time_oscillate)
        print("oscillate 2")
        pin1.write(self.current_adruino_1/ 5.0) # 1
        print("oscillate 3")
        pin2.write(0)
        time.sleep(self.time_oscillate)
        pin1.write(0) 
        pin2.write(self.current_adruino_2/ 5.0) # 1
        print("loop")
    
    '''
    This function implements the loop as it is in the original arduino.
    leftMagnet = the pin the we conent to electromagnet 1.
    rightMagnet = the pin the we conent to electromagnet 2.
    '''
    def arduinoLoop(self, leftMagnet, rightMagnet):
        while (self.flag_arduino_working):
            self.oscillate(leftMagnet, rightMagnet) # 0.5
    
    '''
    Here we initialze the connection with the arduino.
    '''
    def init_arduino(self):
        try:
            self.board = Arduino(Arduino.AUTODETECT)
        except:
            # pop-up window
            msg = QMessageBox()
            msg.setWindowTitle("arduino control")
            msg.setIcon(QMessageBox.Critical)
            msg.setText("problem to find the device")
            x = msg.exec_()

        self.iterator = util.Iterator(self.board)
        self.iterator.start()
        self.leftMagnet = self.board.get_pin('d:11:p')  # digital ('d:13:o')
        self.rightMagnet = self.board.get_pin('d:10:p') # digital ('d:12:o')
    
    '''
    This function returns the last port that was connected to the computer.
    '''
    def find_com_port(self):
        myports = [tuple(p) for p in list(serial.tools.list_ports.comports())]
        return myports[-1][0]
    
    '''
    Turn on the arduino (loop).
    '''
    def run(self): # turn on
        print("arduino turn on")
        self.flag_arduino_working = True 
        self.arduinoLoop(self.leftMagnet, self.rightMagnet)
        
    '''
    Turn off the arduino (loop).
    '''
    def exit2(self): # turn_off
        print("arduino turn off")
        self.flag_arduino_working = False
        time.sleep(1)
        self.board.exit()
        
