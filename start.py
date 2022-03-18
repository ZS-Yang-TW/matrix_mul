
from PyQt5 import QtWidgets
from controller import MainWindow_controller

if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    app.setStyle("fusion")
    window = MainWindow_controller()        #引入controller.py的MainWindow_controller
    window.show()                           #執行並顯示視窗
    sys.exit(app.exec_())                   #按"X"時關閉。