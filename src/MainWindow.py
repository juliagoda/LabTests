# -*- coding: utf-8 -*-

import sys
from mainwindow_ui import Ui_MainWindow
from PyQt5.QtWidgets import QComboBox, QSpinBox, QMainWindow, QApplication, QMessageBox
from PyQt5.QtGui import *
from PyQt5.QtCore import *


class MainWindow(QMainWindow, Ui_MainWindow):
        
    def __init__(self, parent=None):
        super(MainWindow,self).__init__(parent)
        self.setupUi(self)
        self.closeBtn.clicked.connect(self.closeApp)
       # self.checkResultBtn.clicked.connect(lambda: self.checkResult()) # because it expects a callable function

    def closeApp(self):
        self.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MainWindow()
    ex.show()
    sys.exit(app.exec_())


