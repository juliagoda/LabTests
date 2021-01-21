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


from PyQt5.QtWidgets import QMainWindow, QApplication
from mainwindow_ui import Ui_MainWindow
import unittest
import sys

sys.path.append("../ui")  # to see modules in parent's directory


app = QApplication(sys.argv)  # without it we cannot test anything


class MainWindowTest(unittest.TestCase):

    mainwindow = None  # hold QMainWindow in variable
    ui = None   # hold GUI in variable

    def setUp(self):
        self.mainwindow = QMainWindow()  # create empty QMainWindow
        self.ui = Ui_MainWindow()  # we want to test GUI - only
        # set GUI for freshly created QMainWindow
        self.ui.setupUi(self.mainwindow)

    # Check tab names of QTabWidget
    def test_checkTabNames(self):
        self.assertEqual(self.ui.tabWidgetTests.tabText(0),
                         "Complete Blood Count")
        self.assertEqual(self.ui.tabWidgetTests.tabText(1), "Renal Panel")
        self.assertEqual(self.ui.tabWidgetTests.tabText(2), "Liver Panel")
        self.assertEqual(self.ui.tabWidgetTests.tabText(3), "Thyroid Panel")
        self.assertEqual(self.ui.tabWidgetTests.tabText(4),
                         "Electrolyte Panel")
        self.assertEqual(self.ui.tabWidgetTests.tabText(5), "Lipid Panel")

    # Check labels in Complete Blood Count tab
    def test_checkCBCLabels(self):
        self.assertEqual(self.ui.wbcLabel.text(), "WBC")
        self.assertEqual(self.ui.pltLabel.text(), "PLT")
        self.assertEqual(self.ui.hgbLabel.text(), "Hgb")
        self.assertEqual(self.ui.hctLabel.text(), "HCT")
        self.assertEqual(self.ui.rbcLabel.text(), "RBC")

    # Check labels in Renal Panel tab
    def test_checkRenalLabels(self):
        self.assertEqual(self.ui.bunLabel.text(), "BUN")
        self.assertEqual(self.ui.crLabel.text(), "Cr")

    # Check labels in Liver Panel tab
    def test_checkLiverLabels(self):
        self.assertEqual(self.ui.albLabel.text(), "ALB")
        self.assertEqual(self.ui.tbilLabel.text(), "TBIL/SBR")

    # Check labels in Thyroid Panel tab
    def test_checkThyroidLabels(self):
        self.assertEqual(self.ui.tshLabel.text(), "TSH")
        self.assertEqual(self.ui.t3Label.text(), "T3")
        self.assertEqual(self.ui.t4Label.text(), "T4")

    # Check labels in Electrolyte Panel tab
    def test_checkElectrolyteLabels(self):
        self.assertEqual(self.ui.hco3Label.text(), "HCO3")
        self.assertEqual(self.ui.clLabel.text(), "Cl")
        self.assertEqual(self.ui.kLabel.text(), "K")
        self.assertEqual(self.ui.naLabel.text(), "Na")

    # Check labels in Lipid Panel tab
    def test_checkLipidLabels(self):
        self.assertEqual(self.ui.tcLabel.text(), "TC")
        self.assertEqual(self.ui.tgLabel.text(), "TG")
        self.assertEqual(self.ui.hdlLabel.text(), "HDL")
        self.assertEqual(self.ui.ldlLabel.text(), "LDL")

    # Check if amounts widgets for CBC are not disabled
    def test_CBCAmountsEnabled(self):
        self.assertTrue(self.ui.wbcAmountSpinBox.isEnabled())
        self.assertTrue(self.ui.pltAmountSpinBox.isEnabled())
        self.assertTrue(self.ui.hgbAmountSpinBox.isEnabled())
        self.assertTrue(self.ui.hctAmountSpinBox.isEnabled())
        self.assertTrue(self.ui.rbcAmountSpinBox.isEnabled())

        # Check if amounts widgets for Renal Panel are not disabled
    def test_RenalAmountsEnabled(self):
        self.assertTrue(self.ui.bunAmountSpinBox.isEnabled())
        self.assertTrue(self.ui.crAmountSpinBox.isEnabled())

        # Check if amounts widgets for Liver Panel are not disabled
    def test_LiverAmountsEnabled(self):
        self.assertTrue(self.ui.albAmountSpinBox.isEnabled())
        self.assertTrue(self.ui.tbilAmountSpinBox.isEnabled())

        # Check if amounts widgets for Thyroid Panel are not disabled
    def test_ThyroidAmountsEnabled(self):
        self.assertTrue(self.ui.tshAmountSpinBox.isEnabled())
        self.assertTrue(self.ui.t3AmountSpinBox.isEnabled())
        self.assertTrue(self.ui.t4AmountSpinBox.isEnabled())

        # Check if amounts widgets for Electrolyte Panel are not disabled
    def test_ElectrolyteAmountsEnabled(self):
        self.assertTrue(self.ui.hco3AmountSpinBox.isEnabled())
        self.assertTrue(self.ui.clAmountSpinBox.isEnabled())
        self.assertTrue(self.ui.kAmountSpinBox.isEnabled())
        self.assertTrue(self.ui.naAmountSpinBox.isEnabled())

        # Check if amounts widgets for Lipid Panel are not disabled
    def test_LipidAmountsEnabled(self):
        self.assertTrue(self.ui.tcAmountSpinBox.isEnabled())
        self.assertTrue(self.ui.tgAmountSpinBox.isEnabled())
        self.assertTrue(self.ui.hdlAmountSpinBox.isEnabled())
        self.assertTrue(self.ui.ldlAmountSpinBox.isEnabled())

        # Check if units widgets can hold duplicated values
    def test_unitsAmountSetForDupl(self):
        self.assertFalse(self.ui.wbcUnitComboBox.duplicatesEnabled())
        self.assertFalse(self.ui.pltUnitComboBox.duplicatesEnabled())
        self.assertFalse(self.ui.hgbUnitComboBox.duplicatesEnabled())
        self.assertFalse(self.ui.hctUnitComboBox.duplicatesEnabled())
        self.assertFalse(self.ui.rbcUnitComboBox.duplicatesEnabled())

        self.assertFalse(self.ui.bunUnitComboBox.duplicatesEnabled())
        self.assertFalse(self.ui.crUnitComboBox.duplicatesEnabled())

        self.assertFalse(self.ui.albUnitComboBox.duplicatesEnabled())
        self.assertFalse(self.ui.tbilUnitComboBox.duplicatesEnabled())

        self.assertFalse(self.ui.tshUnitComboBox.duplicatesEnabled())
        self.assertFalse(self.ui.t3UnitComboBox.duplicatesEnabled())
        self.assertFalse(self.ui.t4UnitComboBox.duplicatesEnabled())

        self.assertFalse(self.ui.hco3UnitComboBox.duplicatesEnabled())
        self.assertFalse(self.ui.clUnitComboBox.duplicatesEnabled())
        self.assertFalse(self.ui.kUnitComboBox.duplicatesEnabled())
        self.assertFalse(self.ui.kUnitComboBox.duplicatesEnabled())
        self.assertFalse(self.ui.naUnitComboBox.duplicatesEnabled())

        self.assertFalse(self.ui.tcUnitComboBox.duplicatesEnabled())
        self.assertFalse(self.ui.tgUnitComboBox.duplicatesEnabled())
        self.assertFalse(self.ui.hdlUnitComboBox.duplicatesEnabled())
        self.assertFalse(self.ui.ldlUnitComboBox.duplicatesEnabled())

        # Check if amounts widgets for units widgets are not disabled
    def test_unitsAmountEnabled(self):
        self.assertTrue(self.ui.wbcUnitComboBox.isEnabled())
        self.assertTrue(self.ui.pltUnitComboBox.isEnabled())
        self.assertTrue(self.ui.hgbUnitComboBox.isEnabled())
        self.assertTrue(self.ui.hctUnitComboBox.isEnabled())
        self.assertTrue(self.ui.rbcUnitComboBox.isEnabled())

        self.assertTrue(self.ui.bunUnitComboBox.isEnabled())
        self.assertTrue(self.ui.crUnitComboBox.isEnabled())

        self.assertTrue(self.ui.albUnitComboBox.isEnabled())
        self.assertTrue(self.ui.tbilUnitComboBox.isEnabled())

        self.assertTrue(self.ui.tshUnitComboBox.isEnabled())
        self.assertTrue(self.ui.t3UnitComboBox.isEnabled())
        self.assertTrue(self.ui.t4UnitComboBox.isEnabled())

        self.assertTrue(self.ui.hco3UnitComboBox.isEnabled())
        self.assertTrue(self.ui.clUnitComboBox.isEnabled())
        self.assertTrue(self.ui.kUnitComboBox.isEnabled())
        self.assertTrue(self.ui.kUnitComboBox.isEnabled())
        self.assertTrue(self.ui.naUnitComboBox.isEnabled())

        self.assertTrue(self.ui.tcUnitComboBox.isEnabled())
        self.assertTrue(self.ui.tgUnitComboBox.isEnabled())
        self.assertTrue(self.ui.hdlUnitComboBox.isEnabled())
        self.assertTrue(self.ui.ldlUnitComboBox.isEnabled())

        # Check units amount in each QComboBox in QTabWidget
    def test_unitsAmount(self):
        self.assertEqual(self.ui.wbcUnitComboBox.count(), 43)
        self.assertEqual(self.ui.pltUnitComboBox.count(), 43)
        self.assertEqual(self.ui.hgbUnitComboBox.count(), 43)
        self.assertEqual(self.ui.hctUnitComboBox.count(), 43)
        self.assertEqual(self.ui.rbcUnitComboBox.count(), 43)

        self.assertEqual(self.ui.bunUnitComboBox.count(), 43)
        self.assertEqual(self.ui.crUnitComboBox.count(), 43)

        self.assertEqual(self.ui.albUnitComboBox.count(), 43)
        self.assertEqual(self.ui.tbilUnitComboBox.count(), 43)

        self.assertEqual(self.ui.tshUnitComboBox.count(), 43)
        self.assertEqual(self.ui.t3UnitComboBox.count(), 43)
        self.assertEqual(self.ui.t4UnitComboBox.count(), 43)

        self.assertEqual(self.ui.hco3UnitComboBox.count(), 43)
        self.assertEqual(self.ui.clUnitComboBox.count(), 43)
        self.assertEqual(self.ui.kUnitComboBox.count(), 43)
        self.assertEqual(self.ui.kUnitComboBox.count(), 43)
        self.assertEqual(self.ui.naUnitComboBox.count(), 43)

        self.assertEqual(self.ui.tcUnitComboBox.count(), 43)
        self.assertEqual(self.ui.tgUnitComboBox.count(), 43)
        self.assertEqual(self.ui.hdlUnitComboBox.count(), 43)
        self.assertEqual(self.ui.ldlUnitComboBox.count(), 43)

    def test_checkGenderLabel(self):
        self.assertEqual(self.ui.genderLabel.text(), "Gender: ")

    def test_genderOptions(self):
        self.assertEqual(self.ui.genderChoice.itemText(0), "male")
        self.assertEqual(self.ui.genderChoice.itemText(1), "female")

    def test_checkAgeLabel(self):
        self.assertEqual(self.ui.ageLabel.text(), "Age: ")

    # Check max limit for age (54000 is max of days = 150 years)
    def test_ageMaxLimit(self):
        self.assertEqual(self.ui.ageAmountSpinBox.maximum(), 54000)

    def test_ageMinLimit(self):
        self.assertEqual(self.ui.ageAmountSpinBox.minimum(), 0)

    def test_ageOptions(self):
        self.assertEqual(self.ui.ageTypeComboBox.itemText(0), "days")
        self.assertEqual(self.ui.ageTypeComboBox.itemText(1), "months")
        self.assertEqual(self.ui.ageTypeComboBox.itemText(2), "years")

    def test_checkResultBtn(self):
        self.assertEqual(self.ui.checkResultBtn.text(), "Check result")
        self.assertTrue(self.ui.checkResultBtn.isEnabled())

    def test_exitBtn(self):
        self.assertRegex(self.ui.closeBtn.text(), "^(Close|Exit)$")
        self.assertTrue(self.ui.closeBtn.isEnabled())

    def test_menuSettings(self):
        self.assertFalse(self.ui.menuSettings.isEmpty())

        self.assertTrue(self.ui.actionLanguage.isEnabled())
        self.assertTrue(self.ui.actionLanguage.isIconVisibleInMenu())
        self.assertTrue(
            self.ui.actionLanguage.isShortcutVisibleInContextMenu())

        self.assertTrue(self.ui.actionMotiv.isEnabled())
        self.assertTrue(self.ui.actionMotiv.isIconVisibleInMenu())
        self.assertTrue(self.ui.actionMotiv.isShortcutVisibleInContextMenu())

        self.assertTrue(self.ui.actionPrinting.isEnabled())
        self.assertTrue(self.ui.actionPrinting.isIconVisibleInMenu())
        self.assertTrue(
            self.ui.actionPrinting.isShortcutVisibleInContextMenu())

        self.assertTrue(self.ui.actionTabs.isEnabled())
        self.assertTrue(self.ui.actionTabs.isIconVisibleInMenu())
        self.assertTrue(self.ui.actionTabs.isShortcutVisibleInContextMenu())

    def test_menuAboutNotEmpty(self):
        self.assertFalse(self.ui.menuAbout.isEmpty())

        self.assertTrue(self.ui.actionLabtests.isEnabled())
        self.assertTrue(self.ui.actionLanguage.isIconVisibleInMenu())
        self.assertTrue(
            self.ui.actionLanguage.isShortcutVisibleInContextMenu())

        self.assertTrue(self.ui.actionAuthor.isEnabled())
        self.assertTrue(self.ui.actionAuthor.isIconVisibleInMenu())
        self.assertTrue(self.ui.actionAuthor.isShortcutVisibleInContextMenu())

        self.assertTrue(self.ui.actionSources.isEnabled())
        self.assertTrue(self.ui.actionSources.isIconVisibleInMenu())
        self.assertTrue(self.ui.actionSources.isShortcutVisibleInContextMenu())

    def test_menuHelpNotEmpty(self):
        self.assertFalse(self.ui.menuHelp.isEmpty())

        self.assertTrue(self.ui.actionReport_issue.isEnabled())
        self.assertTrue(self.ui.actionReport_issue.isIconVisibleInMenu())
        self.assertTrue(
            self.ui.actionReport_issue.isShortcutVisibleInContextMenu())

        self.assertTrue(self.ui.actionPropose.isEnabled())
        self.assertTrue(self.ui.actionPropose.isIconVisibleInMenu())
        self.assertTrue(self.ui.actionPropose.isShortcutVisibleInContextMenu())

        self.assertTrue(self.ui.actionFAQ.isEnabled())
        self.assertTrue(self.ui.actionFAQ.isIconVisibleInMenu())
        self.assertTrue(self.ui.actionFAQ.isShortcutVisibleInContextMenu())

    def test_labelsToolTips(self):
        self.assertEqual(self.ui.wbcLabel.toolTip(), "White Blood Cells")
        self.assertEqual(self.ui.pltLabel.toolTip(), "Platelets")
        self.assertEqual(self.ui.hgbLabel.toolTip(), "Hgb/Hb - Hemoglobin")
        self.assertEqual(self.ui.hctLabel.toolTip(), "Hematocrit")
        self.assertEqual(self.ui.rbcLabel.toolTip(), "Red Blood Cells")

        self.assertEqual(self.ui.bunLabel.toolTip(), "Blood Urea Nitrogen")
        self.assertEqual(self.ui.crLabel.toolTip(), "Cr / CREAT - Creatinine")

        self.assertEqual(self.ui.albLabel.toolTip(), "Albumin")
        self.assertEqual(self.ui.tbilLabel.toolTip(),
                         "Total Bilirubin / Serum Bilirubin")

        self.assertEqual(self.ui.tshLabel.toolTip(), "Thyroid")
        self.assertEqual(self.ui.t3Label.toolTip(), "Triiodothyronine")
        self.assertEqual(self.ui.t4Label.toolTip(), "Thyroxine")

        self.assertEqual(self.ui.hco3Label.toolTip(), "Bicarbonate")
        self.assertEqual(self.ui.clLabel.toolTip(), "Chloride")
        self.assertEqual(self.ui.kLabel.toolTip(), "Potassium")
        self.assertEqual(self.ui.naLabel.toolTip(), "Sodium")

        self.assertEqual(self.ui.tcLabel.toolTip(), "Total Cholesterol")
        self.assertEqual(self.ui.tgLabel.toolTip(), "Triglycerides")
        self.assertEqual(self.ui.hdlLabel.toolTip(),
                         "High-Density Lipoprotein")
        self.assertEqual(self.ui.ldlLabel.toolTip(), "Low-Density Lipoprotein")
