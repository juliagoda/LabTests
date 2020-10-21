'''
This file is part of LabTests application.

Copyright 2020 Jagoda "juliagoda" Górska.

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU Lesser General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU Lesser General Public License for more details.

You should have received a copy of the GNU Lesser General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.
'''

import sys
import sqlalchemy
from ui.mainwindow_ui import Ui_MainWindow
from PyQt5.QtWidgets import QMainWindow, QApplication


class MainWindow(QMainWindow, Ui_MainWindow):
    
    __connection = None
    
    _bloodDict = {}
    _renalDict = {}
    _liverDict = {}
    _thyroidDict = {}
    _electrolyteDict = {}
    _lipidDict = {}

    def __init__(self, parent=None):
        """Class construction"""
        super(MainWindow,self).__init__(parent)
        self.setupUi(self)
        self.closeBtn.clicked.connect(self.closeApp)
       # self.checkResultBtn.clicked.connect(lambda: self.checkResult()) # because it expects a callable function
       
    def connectDatabase(self):
        """Initiates connection to the database
        """
        self.__connection = sqlalchemy.create_engine("mysql://juliagod_readuser:labtests-heliohost@johnny.heliohost.org:3306/juliagod_labtests", pool_recycle=280).connect()
        
    def saveResultsToDict(self, tabGuiChoices, gender, age, typeAge, dictType):
        """How to transfer data from the main window to global class variables, which are here dictionaries
        
        @type tabGuiChoices: {:[(,,)]}
        @param tabGuiChoices: dictionary with list of tuples with three elements of tab's choices. For example {'Complete Blood Count': [(wbcLabel.text(), wbcUnitComboBox.currentText(), wbcAmountSpinBox.value()), (pltLabel.text(), pltUnitComboBox.currentText(), pltAmountSpinBox.value())]}
        
        @type gender: string
        @param gender: choose between 'male' and 'female'
        
        @type age: unsigned int
        @param age: range 0-9999
        
        @type typeAge: string
        @param typeAge: choose between 'days', 'months' and 'years'
        
        @type dictType: {}
        @param dictType: choose between _bloodDict, _renalDict, _liverDict, _electrolyteDict and _lipidDict
        
        @rtype: bool
        @return: returns the true or false depending on whether any result has been transferred to the dictionary
        """
        
        for tested_aim, desc in tabGuiChoices.items():
            for (shortname, resultAmount, unitname) in desc:
                targetfullname = self.__connection.execute("SELECT `targetfullname` FROM `targetdesc` WHERE `targetshortname` = {shortname}").first()
                statement = self.__connection.execute(getDataQueryText(targetfullname, unitname, typeAge, age, resultAmount, gender)).first() 
                if statement is not None:
                    dictType[tested_aim]['fullname'] = statement['targetfullname']
                    dictType[tested_aim]['down-trend-sympt'] = statement['down-trend-sympt']
                    dictType[tested_aim]['up-trend-sympt'] = statement['up-trend-sympt']
                                                          
        return (len(dictType) > 0)
        
    def getDataQueryText(self, targetfullname, unit, typeAge, age, testsLevel, gender):
        """Returns a complete and prepared request sent to the database based on the arguments
        
        @type targetfullname:
        @param targetfullname:
        
        @type unit: string 
        @param unit: place for the entity related to the results. For example, it could be g/dL, g/L, mg/dL, mcg/dL and so on
        
        @type typeAge: string
        @param typeAge: choose between 'days', 'months' and 'years'
        
        @type age: unsigned int
        @param age: range 0-9999
        
        @type testsLevel: float
        @param testsLevel: the result for a given test
        
        @type gender: string
        @param gender: choose between 'male' and 'female'
        
        @rtype: string
        @return: content of the query
        """
        
        return ("SELECT * FROM `targetdesc` WHERE EXISTS (SELECT 1 FROM `labtests` WHERE `targetdesc`.`targetfullname` = `labtests`.`targetfullname` AND `labtests`.`targetfullname` = {targetfullname} AND `labtests`.`unit` = {unit} AND `labtests`.`age-type` = {typeAge} AND {age} >= `labtests`.`age-range-start` AND {age} <= `labtests`.`age-range-end` AND {testsLevel} >= `labtests`.`normal-range-start` AND {testsLevel} <= `labtests`.`normal-range-end` AND ( `labtests`.`gender` = {gender} XOR `labtests`.`gender` = 'both'))")
        
    def closeDatabase(self):
        if not self.__connection.closed:
            self.__connection.close()

    def closeApp(self):
        self.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MainWindow()
    ex.show()
    sys.exit(app.exec_())


