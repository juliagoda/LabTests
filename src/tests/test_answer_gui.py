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

# To run this: python -m unittest test_mainwindow_gui.py


import sys

sys.path.append("../ui") # to see modules in parent's directory

import unittest
from PyQt5.QtTest import QTest, QSignalSpy
from answer_ui import Ui_Answer
from PyQt5.QtWidgets import QWidget, QApplication


app = QApplication(sys.argv) # without it we cannot test anything


class AnswerWidgetTest(unittest.TestCase):
    
    answerWidget = None  # hold QMainWindow in variable  
    ui = None   # hold GUI in variable
    
    def setUp(self):
        self.answerWidget = QWidget() # create empty QWidget
        self.ui = Ui_Answer() # we want to test GUI - only
        self.ui.setupUi(self.answerWidget) # set GUI for freshly created QMainWindow


    def test_textEditsWidgetsText(self):
        self.assertEqual(self.ui.bloodTextEdit.placeholderText(), "")
        self.assertEqual(self.ui.renalTextEdit.placeholderText(), "")
        self.assertEqual(self.ui.liverTextEdit.placeholderText(), "")
        self.assertEqual(self.ui.thyroidTextEdit.placeholderText(), "")
        self.assertEqual(self.ui.electrolyteTextEdit.placeholderText(), "")
        self.assertEqual(self.ui.lipidTextEdit.placeholderText(), "")

        
    def test_textEditsWidgetsNotDisabled(self):
        self.assertTrue(self.ui.bloodTextEdit.isEnabled())
        self.assertTrue(self.ui.renalTextEdit.isEnabled())
        self.assertTrue(self.ui.liverTextEdit.isEnabled())
        self.assertTrue(self.ui.thyroidTextEdit.isEnabled())
        self.assertTrue(self.ui.electrolyteTextEdit.isEnabled())
        self.assertTrue(self.ui.lipidTextEdit.isEnabled())

        
    def test_textEditsReadOnly(self):
        self.assertTrue(self.ui.bloodTextEdit.isReadOnly())
        self.assertTrue(self.ui.renalTextEdit.isReadOnly())
        self.assertTrue(self.ui.liverTextEdit.isReadOnly())
        self.assertTrue(self.ui.thyroidTextEdit.isReadOnly())
        self.assertTrue(self.ui.electrolyteTextEdit.isReadOnly())
        self.assertTrue(self.ui.lipidTextEdit.isReadOnly())
        
        # try to type "example" into textEdit for blood tests
        QTest.keyClicks(self.ui.bloodTextEdit, "example")
        
        self.assertEqual(self.ui.bloodTextEdit.placeholderText(), "")

        
    def test_changedFontFamily(self):
        signalspy = QSignalSpy(self.ui.fontComboBox.currentIndexChanged)
        self.ui.fontComboBox.setCurrentIndex(2)
        
        # current connections for a signal
        self.assertEqual(self.ui.fontComboBox.receivers(self.ui.fontComboBox.currentIndexChanged), 1)
        
        self.assertEqual(len(signalspy), 1)
        self.assertTrue(signalspy.isValid())
        
        self.assertEqual(self.ui.fontComboBox.currentText(), self.ui.bloodTextEdit.fontFamily())
        self.assertEqual(self.ui.fontComboBox.currentText(), self.ui.renalTextEdit.fontFamily())
        self.assertEqual(self.ui.fontComboBox.currentText(), self.ui.liverTextEdit.fontFamily())
        self.assertEqual(self.ui.fontComboBox.currentText(), self.ui.thyroidTextEdit.fontFamily())
        self.assertEqual(self.ui.fontComboBox.currentText(), self.ui.electrolyteTextEdit.fontFamily())
        self.assertEqual(self.ui.fontComboBox.currentText(), self.ui.lipidTextEdit.fontFamily())
        
        self.ui.fontComboBox.setCurrentIndex(3)
        
        self.assertTrue(signalspy.isValid())
        self.assertEqual(len(signalspy), 2)
        
        self.assertEqual(self.ui.fontComboBox.receivers(self.ui.fontComboBox.currentIndexChanged), 1)
        
        self.assertEqual(self.ui.fontComboBox.currentText(), self.ui.bloodTextEdit.fontFamily())
        self.assertEqual(self.ui.fontComboBox.currentText(), self.ui.renalTextEdit.fontFamily())
        self.assertEqual(self.ui.fontComboBox.currentText(), self.ui.liverTextEdit.fontFamily())
        self.assertEqual(self.ui.fontComboBox.currentText(), self.ui.thyroidTextEdit.fontFamily())
        self.assertEqual(self.ui.fontComboBox.currentText(), self.ui.electrolyteTextEdit.fontFamily())
        self.assertEqual(self.ui.fontComboBox.currentText(), self.ui.lipidTextEdit.fontFamily())
        
        for signal in signalspy:
            print("That was argument's value during setCurrentIndex (for font family change) execution: ", signal[0], "\n")
            print("So the font family changed to ", self.ui.fontComboBox.itemText(signal[0]), "\n")


    def test_closeBtnNotDisabled(self):
        self.assertTrue(self.ui.returnBtn.isEnabled())
        
    def test_printBtnNotDisabled(self):
        self.assertTrue(self.ui.printBtn.isEnabled())
        