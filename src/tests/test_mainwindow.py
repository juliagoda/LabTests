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

# To run this: python -m unittest test_mainwindow.py


from PyQt5.QtWidgets import QMainWindow, QApplication
from MainWindow import MainWindow
import unittest
import sys

sys.path.append("../")  # to see modules in parent's directory


app = QApplication(sys.argv)  # without it we cannot test anything


class MainWindowTest(unittest.TestCase):

    mainwindow = None  # hold MainWindow
    maxDiff = None

    @classmethod
    def setUp(self):
        self.mainwindow = MainWindow()
        self.mainwindow.connectDatabase()

    def test_connectDatabase(self):
        self.assertTrue(self.mainwindow.getEngine().has_table("labtests"))
        self.assertTrue(self.mainwindow.getEngine().has_table("targetdesc"))

    def test_getDataQueryText(self):
        schema = "SELECT * FROM `targetdesc` WHERE EXISTS (SELECT 1 FROM `labtests` WHERE `targetdesc`.`targetfullname` = `labtests`.`targetfullname` AND `labtests`.`targetfullname` = 'White Blood Cells' AND `labtests`.`unit` = 'g/L' AND `labtests`.`age-type` = 'days' AND 2 >= `labtests`.`age-range-start` AND 2 <= `labtests`.`age-range-end` AND 10 >= `labtests`.`normal-range-start` AND 10 <= `labtests`.`normal-range-end` AND ( `labtests`.`gender` = 'female' XOR `labtests`.`gender` = 'both'))"

        result = self.mainwindow.getDataQueryText(
            'White Blood Cells', 'g/L', 'days', 2, 10, 'female')
        self.assertEqual(schema, result)

    def test_saveResultsToDict(self):
        result = self.mainwindow.saveResultsToDict({'Complete Blood Count': [(
            'WBC', 10, 'g/L')]}, 'female', 2, 'days', self.mainwindow.getBloodDict())
        self.assertTrue(result)

    @classmethod
    def tearDownClass(self):
        if not self.mainwindow.getConnection().closed:
            self.mainwindow.getConnection().close()
