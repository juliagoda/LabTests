# -*- coding: utf-8 -*-

from PyQt5.QtWidgets import QDoubleSpinBox, QGroupBox, QLabel, QMainWindow, QMessageBox, QWidget
from PyQt5.QtCore import *
from BaseOrgan import Organ
from string import digits


class bloodMorph(Organ):
    
    _bloodMorphDict = {}
    'derived class from Blood class for morphology blood part'
    
    def __init__(self, mainWindow):
        self._setBuddies(mainWindow)
        listBoxes = self._createListOfAllBoxes(mainWindow)
        listLabels = self._createListOfAllLabels(mainWindow)
        
        for bloodMeasure in listBoxes:
            if (self._foundMoreDescThanOne(bloodMeasure)):
                self._showWarningAndAbort(mainWindow)
                return
        
        for bloodAbbr in listLabels:
            objNameBuddy = bloodAbbr.buddy().objectName()
            for bloodMeasure in listBoxes:
                if (bloodMeasure.objectName() == objNameBuddy):
                    if (bloodMeasure.value() > 0):
                        self._bloodMorphDict[bloodAbbr.text().replace('&','').strip()] = str(repr(bloodMeasure.value())).strip() + ' ' + bloodMeasure.suffix().strip()
        
        self._organDict['Blood-Morphology'] = self._bloodMorphDict
        self.showAllBloodMorphDictElemKey()
        self.showAllDictElemKey()
                
    
    def getBloodMorphDict(self):
        return self._bloodMorphDict
    
    def lenOfMorphDict(self):
        return len(self._bloodMorphDict)
    
    def showAllBloodMorphDictElemKey(self):
        print(["[ " + key1 + " ] = " + value1 for key1, value1 in self._bloodMorphDict.items()])
    
    def _setBuddies(self, uiwindow):
        if (uiwindow.MorphBloodRBC1.value() == 0 and uiwindow.MorphBloodRBC2.value() > 0):
            uiwindow.RBCBloodLabel.setBuddy(uiwindow.MorphBloodRBC2)
            
        if (uiwindow.MorphBloodHGB1.value() == 0 and uiwindow.MorphBloodHGB2.value() > 0):
            uiwindow.HGBBloodLabel.setBuddy(uiwindow.MorphBloodHGB2)
            
        if (uiwindow.MorphBloodMCHC1.value() == 0 and uiwindow.MorphBloodMCHC2.value() > 0):
            uiwindow.MCHCBloodLabel.setBuddy(uiwindow.MorphBloodMCHC2)
            
        if (uiwindow.MorphBloodWBC1.value() == 0 and uiwindow.MorphBloodWBC2.value() > 0):
            uiwindow.WBCBloodLabel.setBuddy(uiwindow.MorphBloodWBC2)
            
        if (uiwindow.MorphBloodLYM1.value() == 0 and uiwindow.MorphBloodLYM2.value() > 0):
            uiwindow.LYMBloodLabel.setBuddy(uiwindow.MorphBloodLYM2)
        elif (uiwindow.MorphBloodLYM2.value() == 0 and uiwindow.MorphBloodLYM3.value() > 0):
            uiwindow.LYMBloodLabel.setBuddy(uiwindow.MorphBloodLYM3)
            
        if (uiwindow.MorphBloodMONO1.value() == 0 and uiwindow.MorphBloodMONO2.value() > 0):
            uiwindow.MONOBloodLabel.setBuddy(uiwindow.MorphBloodMONO2)
            
        if (uiwindow.MorphBloodPLT1.value() == 0 and uiwindow.MorphBloodPLT2.value() > 0):
            uiwindow.PLTBloodLabel.setBuddy(uiwindow.MorphBloodPLT2)
    
    
    def _createListOfAllBoxes(self, uiwindow):
        print(len(uiwindow.morphologyGroupBox.findChildren(QDoubleSpinBox)))
        return uiwindow.morphologyGroupBox.findChildren(QDoubleSpinBox)
    
    def _createListOfAllLabels(self, uiwindow):
        print(len(uiwindow.morphologyGroupBox.findChildren(QLabel)))
        return uiwindow.morphologyGroupBox.findChildren(QLabel)
    
    def _showWarningAndAbort(self,uiwindow):
        QMessageBox.warning(uiwindow,"Duplication","Various measurement type values for the same test cannot be set. Make a choice and choose only one measurement for your test in blood morphology part (for example only M/μl for RBC in blood morphology)")
        return  
    


class bloodWCC(Organ):
    
    'derived class from Blood class for WCC blood part'
    _bloodWCCDict = {}
    
    def __init__(self, mainWindow):
        self._setBuddies(mainWindow)
        listBoxes = self._createListOfAllBoxes(mainWindow)
        listLabels = self._createListOfAllLabels(mainWindow)
        
        for bloodMeasure in listBoxes:
            if (self._foundMoreDescThanOne(bloodMeasure)):
                self._showWarningAndAbort(mainWindow)
                return
            
        for bloodAbbr in listLabels:
            objNameBuddy = bloodAbbr.buddy().objectName()
            for bloodMeasure in listBoxes:
                if (bloodMeasure.objectName() == objNameBuddy):
                    if (bloodMeasure.value() > 0):
                        self._bloodWCCDict[bloodAbbr.text().replace('&','').strip()] = str(repr(bloodMeasure.value())).strip() + ' ' + bloodMeasure.suffix().strip()
        
        self._organDict['Blood-WCC'] = self._bloodWCCDict
        self.showAllBloodWCCDictElemKey()
        self.showAllDictElemKey()
                
    
    def getBloodWCCDict(self):
        return self._bloodWCCDict
    
    def lenOfWCCDict(self):
        return len(self._bloodWCCDict)
    
    def showAllBloodWCCDictElemKey(self):
        print(["[ " + key1 + " ] = " + value1 for key1, value1 in self._bloodWCCDict.items()])
    
    def _setBuddies(self, uiwindow):
        if (uiwindow.WCCBloodNeut1.value() == 0 and uiwindow.WCCBloodNeut2.value() > 0):
            uiwindow.NEUTNEBloodLabel.setBuddy(uiwindow.WCCBloodNeut2)
            
        if (uiwindow.WCCBloodEOS1.value() == 0 and uiwindow.WCCBloodEOS2.value() > 0):
            uiwindow.EOSBloodLabel.setBuddy(uiwindow.WCCBloodEOS2)
            
        if (uiwindow.WCCBloodBASO1.value() == 0 and uiwindow.WCCBloodBASO2.value() > 0):
            uiwindow.BASOBloodLabel.setBuddy(uiwindow.WCCBloodBASO2)
    
    
    def _createListOfAllBoxes(self, uiwindow):
        print(len(uiwindow.wccGroupBox.findChildren(QDoubleSpinBox)))
        return uiwindow.wccGroupBox.findChildren(QDoubleSpinBox)
    
    def _createListOfAllLabels(self, uiwindow):
        print(len(uiwindow.wccGroupBox.findChildren(QLabel)))
        return uiwindow.wccGroupBox.findChildren(QLabel)
    
    def _showWarningAndAbort(self,uiwindow):
        QMessageBox.warning(uiwindow,"Duplication","Various measurement type values for the same test cannot be set. Make a choice and choose only one measurement for your test in blood WCC part (for example only K/μl (G/l) for NEUT/NE in blood WCC)")
        return 


class bloodBioChem(Organ):
    
    'derived class from Blood class for biochemistry blood part'
    _bloodBioDict = {}
    
    def __init__(self, mainWindow):
        self._setBuddies(mainWindow)
        listBoxes = self._createListOfAllBoxes(mainWindow)
        listLabels = self._createListOfAllLabels(mainWindow)
        
        for bloodMeasure in listBoxes:
            if (self._foundMoreDescThanOne(bloodMeasure)):
                self._showWarningAndAbort(mainWindow)
                return
            
        for bloodAbbr in listLabels:
            objNameBuddy = bloodAbbr.buddy().objectName()
            for bloodMeasure in listBoxes:
                if (bloodMeasure.objectName() == objNameBuddy):
                    if (bloodMeasure.value() > 0):
                        self._bloodBioDict[bloodAbbr.text().replace('&','').strip()] = str(repr(bloodMeasure.value())).strip() + ' ' + bloodMeasure.suffix().strip()
        
        self._organDict['Blood-Bio'] = self._bloodBioDict
        self.showAllBloodBioDictElemKey()
        self.showAllDictElemKey()
                
    
    def getBloodBioDict(self):
        return self._bloodBioDict
    
    def lenOfBioDict(self):
        return len(self._bloodBioDict)
    
    def showAllBloodBioDictElemKey(self):
        print(["[ " + key1 + " ] = " + value1 for key1, value1 in self._bloodBioDict.items()])
    
    def _setBuddies(self, uiwindow):
        if (uiwindow.BioBloodALAT1.value() == 0 and uiwindow.BioBloodALAT2.value() > 0):
            uiwindow.ALATBloodLabel.setBuddy(uiwindow.BioBloodALAT2)
            
        if (uiwindow.BioBloodAspAT1.value() == 0 and uiwindow.BioBloodAspAT2.value() > 0):
            uiwindow.AspATBloodLabel.setBuddy(uiwindow.BioBloodAspAT2)
            
        if (uiwindow.BioBloodBcTp1.value() == 0 and uiwindow.BioBloodBcTp2.value() > 0):
            uiwindow.BcTpBloodLabel.setBuddy(uiwindow.BioBloodBcTp2)
            
        if (uiwindow.BioBloodBILT1.value() == 0 and uiwindow.BioBloodBILT2.value() > 0):
            uiwindow.BILTBloodLabel.setBuddy(uiwindow.BioBloodBILT2)
            
        if (uiwindow.BioBloodHDL1.value() == 0 and uiwindow.BioBloodHDL2.value() > 0):
            uiwindow.HDLBloodLabel.setBuddy(uiwindow.BioBloodHDL2)
            
        if (uiwindow.BioBloodLDL1.value() == 0 and uiwindow.BioBloodLDL2.value() > 0):
            uiwindow.LDLBloodLabel.setBuddy(uiwindow.BioBloodLDL2)

        if (uiwindow.BioBloodCHOL1.value() == 0 and uiwindow.BioBloodCHOL2.value() > 0):
            uiwindow.CHOLBloodLabel.setBuddy(uiwindow.BioBloodCHOL2)

        if (uiwindow.BioBloodFibr1.value() == 0 and uiwindow.BioBloodFibr2.value() > 0):
            uiwindow.FIBRBloodLabel.setBuddy(uiwindow.BioBloodFibr2)

        if (uiwindow.BioBloodP1.value() == 0 and uiwindow.BioBloodP2.value() > 0):
            uiwindow.PBloodLabel.setBuddy(uiwindow.BioBloodP2)
            
        if (uiwindow.BioBloodGLU1.value() == 0 and uiwindow.BioBloodGLU2.value() > 0):
            uiwindow.GLUBloodLabel.setBuddy(uiwindow.BioBloodGLU2)
            
        if (uiwindow.BioBloodCREA1.value() == 0 and uiwindow.BioBloodCREA2.value() > 0):
            uiwindow.CREABloodLabel.setBuddy(uiwindow.BioBloodCREA2)
            
        if (uiwindow.BioBloodURIC1.value() == 0 and uiwindow.BioBloodURIC2.value() > 0):
            uiwindow.URICBloodLabel.setBuddy(uiwindow.BioBloodURIC2)
            
        if (uiwindow.BioBloodTG1.value() == 0 and uiwindow.BioBloodTG2.value() > 0):
            uiwindow.TGBloodLabel.setBuddy(uiwindow.BioBloodTG2)
            
        if (uiwindow.BioBloodUREA1.value() == 0 and uiwindow.BioBloodUREA2.value() > 0):
            uiwindow.UREABloodLabel.setBuddy(uiwindow.BioBloodUREA2)
            
        if (uiwindow.BioBloodCa1.value() == 0 and uiwindow.BioBloodCa2.value() > 0):
            uiwindow.CaBloodLabel.setBuddy(uiwindow.BioBloodCa2)
    
    
    def _createListOfAllBoxes(self, uiwindow):
        print("Length of Boxes in Blood Bio part: " + str(len(uiwindow.bloodBioChemGroupBox.findChildren(QDoubleSpinBox))))
        return uiwindow.bloodBioChemGroupBox.findChildren(QDoubleSpinBox)
    
    def _createListOfAllLabels(self, uiwindow):
        print("Length of Labels in Blood Bio part: " + str(len(uiwindow.bloodBioChemGroupBox.findChildren(QLabel))))
        return uiwindow.bloodBioChemGroupBox.findChildren(QLabel)
    
    def _showWarningAndAbort(self,uiwindow):
        QMessageBox.warning(uiwindow,"Duplication","Various measurement type values for the same test cannot be set. Make a choice and choose only one measurement for your test in blood biochemistry part (for example only mg/dl for BIL-T in blood biochemistry)")
        return 
