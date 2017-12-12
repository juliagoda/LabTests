# -*- coding: utf-8 -*-

import sys
from ui.answer_ui import Ui_Answer
from PyQt5.QtWidgets import QWidget, QTextEdit


class Answer(QWidget, Ui_Answer):
    
    def __init__(self,resultsDict):
        super(Answer,self).__init__()
        self.setupUi(self)
        self.returnBtn.clicked.connect(self.__returnToMainWindow)
        
        self.textEditBlood.setText(self.__prepareContentOrgan(resultsDict, "Blood"))
        self.textEditUrine.setText(self.__prepareContentOrgan(resultsDict, "Urine"))
        self.textEditLiver.setText(self.__prepareContentOrgan(resultsDict, "Liver"))
        
        
    def __returnToMainWindow(self):
        self.textEditBlood.clear()
        self.textEditUrine.clear()
        self.textEditLiver.clear()
        self.close()
        
    def __getOrganName(self, elemString):
        return elemString.split('-', 1)[0]
        
    def __prepareContentOrgan(self, resultsDict, organ):
        text = ""
        for k, v in resultsDict.items():
            if (self.__getOrganName(k) == organ):
                text += str(v) + "\n"
                
        return text
                
