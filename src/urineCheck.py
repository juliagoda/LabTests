# -*- coding: utf-8 -*-

from PyQt5.QtWidgets import QDoubleSpinBox, QGroupBox, QLabel, QMainWindow, QMessageBox, QWidget, QComboBox
from PyQt5.QtCore import *
from BaseOrgan import Organ
from string import digits


class urineBioChem(Organ):
    
    'derived class from Urine class for biochemistry urine part'
    _urineBioDict = {}
    
    def __init__(self, mainWindow):
        self._setBuddies(mainWindow)
        listBoxes = self._createListOfAllBoxes(mainWindow)
        listLabels = self._createListOfAllLabels(mainWindow)
        
        for urineMeasure in listBoxes:
            if (self._foundMoreDescThanOne(urineMeasure)):
                self._showWarningAndAbort(mainWindow)
                return
            
        for urineAbbr in listLabels:
            objNameBuddy = urineAbbr.buddy().objectName()
            for urineMeasure in listBoxes:
                if (urineMeasure.objectName() == objNameBuddy):
                    if (urineMeasure.value() > 0):
                        self._urineBioDict[urineAbbr.text().replace('&','').strip()] = str(repr(urineMeasure.value())).strip() + ' ' + urineMeasure.suffix().strip()
        
        self._organDict['Urine-Bio'] = self._urineBioDict
        self.showAllBioDictUrineElemKey()
        self.showAllDictElemKey()
                
    
    def getUrineBioDict(self):
        return self._urineBioDict
    
    def lenOfBioUrineDict(self):
        return len(self._urineBioDict)
    
    def showAllBioDictUrineElemKey(self):
        print(["[ " + key1 + " ] = " + value1 for key1, value1 in self._urineBioDict.items()])
    
    def _setBuddies(self, uiwindow):
        if (uiwindow.BioUrineCreat1.value() == 0 and uiwindow.BioUrineCreat2.value() > 0):
            uiwindow.CREATUrineLabel.setBuddy(uiwindow.BioUrineCreat2)
        elif (uiwindow.BioUrineCreat2.value() == 0 and uiwindow.BioUrineCreat3.value() > 0):
            uiwindow.CREATUrineLabel.setBuddy(uiwindow.BioUrineCreat3)
        elif (uiwindow.BioUrineCreat3.value() == 0 and uiwindow.BioUrineCreat4.value() > 0):
            uiwindow.CREATUrineLabel.setBuddy(uiwindow.BioUrineCreat4)
            
        if (uiwindow.BioUrineUREA1.value() == 0 and uiwindow.BioUrineUREA2.value() > 0):
            uiwindow.UREAUrineLabel.setBuddy(uiwindow.BioUrineUREA2)
            
        if (uiwindow.BioUrineGLU1.value() == 0 and uiwindow.BioUrineGLU2.value() > 0):
            uiwindow.GLUrineLabel.setBuddy(uiwindow.BioUrineGLU2)
            
        if (uiwindow.BioUrineURIC1.value() == 0 and uiwindow.BioUrineURIC2.value() > 0):
            uiwindow.URICUrineLabel.setBuddy(uiwindow.BioUrineURIC2)
            
        if (uiwindow.BioUrineBIL1.value() == 0 and uiwindow.BioUrineBIL2.value() > 0):
            uiwindow.BILUrineLabel.setBuddy(uiwindow.BioUrineBIL2)
            
        if (uiwindow.BioUrineBILT1.value() == 0 and uiwindow.BioUrineBILT2.value() > 0):
            uiwindow.BILTUrineLabel.setBuddy(uiwindow.BioUrineBILT2)
    
    
    def _createListOfAllBoxes(self, uiwindow):
        print("Length of Boxes in Urine Bio part: " + str(len(uiwindow.urineBioChemGroupBox.findChildren(QDoubleSpinBox))))
        return uiwindow.urineBioChemGroupBox.findChildren(QDoubleSpinBox)
    
    def _createListOfAllLabels(self, uiwindow):
        print("Length of Labels in Urine Bio part: " + str(len(uiwindow.urineBioChemGroupBox.findChildren(QLabel))))
        return uiwindow.urineBioChemGroupBox.findChildren(QLabel)
    
    def _showWarningAndAbort(self,uiwindow):
        QMessageBox.warning(uiwindow,"Duplication","Various measurement type values for the same test cannot be set. Make a choice and choose only one measurement for your test in urine biochemistry part (for example only mmol/l for UREA in urine biochemistry)")
        return 
    
    
    
class urineGeneral(Organ):
    
    _urineGenDict = {}
    'derived class from Urine class for general urine part'
    
    def __init__(self, mainWindow):
        listBoxes = self._createListOfAllBoxes(mainWindow)
        listCombos = self._createListOfAllCombos(mainWindow)
        listLabels = self._createListOfAllLabels(mainWindow)
        
       #'Temporarily there are no choices between measurements for any labels'
       # for urineMeasure in listBoxes:
       #     if (self._foundMoreDescThanOne(urineMeasure)):
       #         self._showWarningAndAbort(mainWindow)
       #         return
        
        for urineAbbr in listLabels:
            objNameBuddy = urineAbbr.buddy().objectName()
            for urineMeasure in listBoxes:
                if (urineMeasure.objectName() == objNameBuddy):
                    if (urineMeasure.value() > 0):
                        self._urineGenDict[urineAbbr.text().replace('&','').strip()] = str(repr(urineMeasure.value())).strip() + ' ' + urineMeasure.suffix().strip()
            for urineChoice in listCombos:
                if (urineChoice.objectName() == objNameBuddy):
                    if (urineChoice.currentIndex() < 2):
                        self._urineGenDict[urineAbbr.text().replace('&','').strip()] = urineChoice.currentText().strip()
                    
                    
        self._organDict['Urine-General'] = self._urineGenDict
        self.showAllGenDictUrineElemKey()
        self.showAllDictElemKey()
                
    
    def getUrineGenDict(self):
        return self._urineGenDict
    
    def lenOfUrineGenDict(self):
        return len(self._urineGenDict)
    
    def showAllGenDictUrineElemKey(self):
        print(["[ " + key1 + " ] = " + value1 for key1, value1 in self._urineGenDict.items()])
    
    
    def _createListOfAllBoxes(self, uiwindow):
        print(len(uiwindow.urineGenGroupBox.findChildren(QDoubleSpinBox)))
        return uiwindow.urineGenGroupBox.findChildren(QDoubleSpinBox)
    
    def _createListOfAllCombos(self, uiwindow):
        print(len(uiwindow.urineGenGroupBox.findChildren(QComboBox)))
        return uiwindow.urineGenGroupBox.findChildren(QComboBox)
    
    def _createListOfAllLabels(self, uiwindow):
        print(len(uiwindow.urineGenGroupBox.findChildren(QLabel)))
        return uiwindow.urineGenGroupBox.findChildren(QLabel)
    
    def _showWarningAndAbort(self,uiwindow):
        QMessageBox.warning(uiwindow,"Duplication","Various measurement type values for the same test cannot be set. Make a choice and choose only one measurement for your test in urine general part")
        return  