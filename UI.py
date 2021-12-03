# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'day13.ui'
#
# Created by: PyQt5 UI code generator 5.12.3
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1980, 1023)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.button_1 = QtWidgets.QPushButton(self.centralwidget)
        self.button_1.setGeometry(QtCore.QRect(50, 910, 201, 51))
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.button_1.setFont(font)
        self.button_1.setObjectName("button_1")
        self.button_2 = QtWidgets.QPushButton(self.centralwidget)
        self.button_2.setGeometry(QtCore.QRect(280, 910, 201, 51))
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.button_2.setFont(font)
        self.button_2.setObjectName("button_2")
        self.label_showsize = QtWidgets.QLabel(self.centralwidget)
        self.label_showsize.setGeometry(QtCore.QRect(1020, 910, 481, 51))
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(12)
        self.label_showsize.setFont(font)
        self.label_showsize.setObjectName("label_showsize")
        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea.setGeometry(QtCore.QRect(40, 30, 831, 801))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setFixedSize(161,301)
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.label_picture = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_picture.setGeometry(QtCore.QRect(20, 10, 161, 301))
        self.label_picture.setObjectName("label_picture")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1980, 18))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.button_1.setText(_translate("MainWindow", "放大 (Zoom in)"))
        self.button_2.setText(_translate("MainWindow", "縮小 (Zoom out)"))
        self.label_showsize.setText(_translate("MainWindow", "當前大小:"))
        self.label_picture.setText(_translate("MainWindow", "TextLabel"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
