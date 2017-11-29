# -*- coding: utf-8 -*-

from PyQt5.QtWidgets import QDoubleSpinBox, QGroupBox, QLabel, QMainWindow, QMessageBox, QWidget
from PyQt5.QtCore import *
from BaseOrgan import Organ
from string import digits

        
class liverFuncTest(Organ):
    
    _liverFuncTestDict = {}
    'derived class from Liver class for function test liver part'
    
    def __init__(self, mainWindow):
        self._setBuddies(mainWindow)
        listBoxes = self._createListOfAllBoxes(mainWindow)
        listLabels = self._createListOfAllLabels(mainWindow)
        
        for liverMeasure in listBoxes:
            if (self._foundMoreDescThanOne(liverMeasure)):
                self._showWarningAndAbort(mainWindow)
                return
        
        for liverAbbr in listLabels:
            objNameBuddy = liverAbbr.buddy().objectName()
            for liverMeasure in listBoxes:
                if (liverMeasure.objectName() == objNameBuddy):
                    if (liverMeasure.value() > 0):
                        self._liverFuncTestDict[liverAbbr.text().replace('&','').strip()] = str(repr(liverMeasure.value())).strip() + ' ' + liverMeasure.suffix().strip()
        
        self._organDict['Liver-Test'] = self._liverFuncTestDict
        self.showAllLiverTestDictElemKey()
        self.showAllDictElemKey()
                
    
    def getLiverTestDict(self):
        return self._liverFuncTestDict
    
    def lenOfLiverTestDict(self):
        return len(self._liverFuncTestDict)
    
    def showAllLiverTestDictElemKey(self):
        print(["[ " + key1 + " ] = " + value1 for key1, value1 in self._liverFuncTestDict.items()])
    
    def _setBuddies(self, uiwindow):
        if (uiwindow.FuncLiverBILT1.value() == 0 and uiwindow.FuncLiverBILT2.value() > 0):
            uiwindow.BILTLiverLabel.setBuddy(uiwindow.FuncLiverBILT2)
    
    def _createListOfAllBoxes(self, uiwindow):
        print(len(uiwindow.liverTestsGroupBox.findChildren(QDoubleSpinBox)))
        return uiwindow.liverTestsGroupBox.findChildren(QDoubleSpinBox)
    
    def _createListOfAllLabels(self, uiwindow):
        print(len(uiwindow.liverTestsGroupBox.findChildren(QLabel)))
        return uiwindow.liverTestsGroupBox.findChildren(QLabel)
    
    def _showWarningAndAbort(self,uiwindow):
        QMessageBox.warning(uiwindow,"Duplication","Various measurement type values for the same test cannot be set. Make a choice and choose only one measurement for your test in liver test function part (for example only mg% for BIL-T in liver function test)")
        return