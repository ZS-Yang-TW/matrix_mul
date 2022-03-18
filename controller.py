from concurrent.futures import thread
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtMultimedia import *
from PyQt5.QtMultimediaWidgets import *

from UI import Ui_MainWindow                    #UI介面
from ConnectDatabase import database            #建立連線的需求
from os import system

class ThreadTask(QThread):
    def run(self):
        system('python Matrix_calculator.py')
        self.__del__()
        system('manim matrix_mul.py -pqm')

    def __del__(self):
        print ("Done!")

#Main_Function
class MainWindow_controller(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__() # in python3, super(Class, self).xxx = super().xxx
        self.ui = Ui_MainWindow() 
        self.ui.setupUi(self)
        self.setup_control()


    def setup_control(self):
        WEB_matrix = ThreadTask()
        WEB_matrix.start()
        
        