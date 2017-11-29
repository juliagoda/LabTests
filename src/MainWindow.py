# -*- coding: utf-8 -*-

import sys
from ui.mainwindow_ui import Ui_MainWindow
from bloodCheck import bloodMorph, bloodWCC, bloodBioChem
from urineCheck import urineBioChem, urineGeneral
from liverCheck import liverFuncTest
from BaseOrgan import Organ
from Summary import Summary
from answer import Answer
from PyQt5.QtWidgets import QComboBox, QSpinBox, QMainWindow, QApplication, QMessageBox
from PyQt5.QtGui import *
from PyQt5.QtCore import *


class MainWindow(QMainWindow, Ui_MainWindow):
    
    __personDict = {}
    
    def __init__(self, parent=None):
        super(MainWindow,self).__init__(parent)
        self.setupUi(self)
        self.closeBtn.clicked.connect(self.closeApp)
        self.checkResultBtn.clicked.connect(lambda: self.checkResult()) # because it expects a callable function

    def closeApp(self):
        self.close()
        
    def warnNotCheckedGender(self):
        if (self.dayAgeInput.value() == 0 and self.monthAgeInput.value() == 0 and self.yearAgeInput.value() == 0):
            QMessageBox.warning(self, "Age", "Age hasn't been set. You should set days, months or years in age part")
            return
            
        if (self.genderChoice.currentIndex() == -1):
            QMessageBox.warning(self, "Gender", "Combo Box with gender choice is empty or current text is empty")
            return
        
    def getAge(self):
        if (self.dayAgeInput.value() != 0):
            self.__personDict['Age-Days'] = self.dayAgeInput.value()
        elif (self.monthAgeInput.value() != 0):
            self.__personDict['Age-Months'] = self.monthAgeInput.value()
        elif (self.yearAgeInput.value() != 0):
            self.__personDict['Age-Years'] = self.yearAgeInput.value()
        
    def checkResult(self):
        self.update()
        self.warnNotCheckedGender()
        bloodMorph(self)
        bloodWCC(self)
        bloodBioChem(self)
        urineBioChem(self)
        urineGeneral(self)
        liverFuncTest(self)
        self.__personDict['Gender'] = self.genderChoice.currentText() 
        self.getAge()

        self.organ = Organ()
        self.summary = Summary(self.organ.getAllDict(),self.__personDict)
        self.answer = Answer(self.summary.getResultsDict())
        self.answer.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MainWindow()
    ex.show()
    sys.exit(app.exec_())


