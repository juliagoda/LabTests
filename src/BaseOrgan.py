from PyQt5.QtWidgets import QDoubleSpinBox
from PyQt5.QtCore import *
from string import digits


class Organ():
    
    _organDict = {}
    'base class for organ tests'
    
    def __init__(self): 
        pass

    def getAllDict(self):
        return self._organDict
    
    def clearAllDict(self):
        self._organDict.clear()

    def getAllElemLen(self):
        return len(self._organDict)
    
    def showAllDictElemKey(self):
        print([["[ " + key1 + " ][ " + key2 + " ] = " + value2 
                for key2, value2 in value1.items()]
                for key1, value1 in self._organDict.items()])
        
    def __getitem__(self,index):
        return self._organDict[index]

    def __checkOtherLayChild(self, qdSpinBox):
        getChar = qdSpinBox.objectName()[-1:]
        print("If " + str(getChar) + " is digit")
        if (getChar.isdigit()):
            return True
        else:
            return False
        
    def __addToStrList(self, qdSpinBox):
        if (self.__checkOtherLayChild(qdSpinBox)):
            print("Char was digit")
            remove_digits = str.maketrans('', '', digits)
            res = qdSpinBox.objectName().translate(remove_digits)
            listChild = qdSpinBox.parentWidget().findChildren(QDoubleSpinBox,QRegExp("^" + res))
            print("count of QDoubleSpinBox with begin of name: " + res)
            print("number of QDoubleSpinBoxes with tha name at the beginning: " + str(len(listChild)))
            return listChild
        else:
            return []
            
        
    def _foundMoreDescThanOne(self, qdSpinBox):
        listFromBoxes = self.__addToStrList(qdSpinBox)
        print("In foundMoreDescThanOne function number of list with QDoubleSpinBoxes matched to name at beginning: " + str(len(listFromBoxes)))
        if (len(listFromBoxes) > 0):
            i = 0
            for douSpinBox in listFromBoxes:
                print("objectName of spinBox from listFromBoxes: " + douSpinBox.objectName())
                print("value of spinBox from listFromBoxes: " + str(douSpinBox.value()))
                if (douSpinBox.value() != 0):
                    i = i + 1
                    print("i of iteration after adding: " + str(i))
                    if (i > 1):
                        print("There is a duplication of measurement for the same label!")
                        return True
            if (i >= len(listFromBoxes)):
                print("i of iteration is more or equal to list count: " + str(i))
                return False
        else:
            return False 
