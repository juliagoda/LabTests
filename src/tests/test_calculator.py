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


import unittest
from Calculator import Calculator


class TestCalculator(unittest.TestCase):

    def test_divByTen(self):
        calc = Calculator()
        numb = 20
        self.assertEqual(calc.divByTen(numb), 2)

    def test_multByTen(self):
        calc = Calculator()
        numb = 20
        self.assertEqual(calc.multByTen(numb), 200)

    def test_divBy100(self):
        calc = Calculator()
        numb = 1
        self.assertEqual(calc.divBy100(numb), 0.01)

    def test_multBy100(self):
        calc = Calculator()
        numb = 1
        self.assertEqual(calc.multBy100(numb), 100)

    def test_divBy1000(self):
        calc = Calculator()
        numb = 1
        self.assertEqual(calc.divBy1000(numb), 0.001)

    def test_multBy1000(self):
        calc = Calculator()
        numb = 1
        self.assertEqual(calc.multBy1000(numb), 1000)

    def test_divBy1000000(self):
        calc = Calculator()
        numb = 1
        self.assertEqual(calc.divBy1000000(numb), 0.000001)

    def test_multBy1000000(self):
        calc = Calculator()
        numb = 1
        self.assertEqual(calc.multBy1000000(numb), 1000000)

    def test_gdlToMmolForHgb(self):
        calc = Calculator()
        numb = 2
        self.assertEqual(calc.gdlToMmolForHgb(numb), 0.31)

    def test_mmolToGdlForHgb(self):
        calc = Calculator()
        numb = 2
        self.assertEqual(calc.mmolToGdlForHgb(numb), 12.90)

    def test_percentToLLForHct(self):
        calc = Calculator()
        numb = 2
        self.assertEqual(calc.percentToLLForHct(numb), 0.02)

    def test_llToPercentForHct(self):
        calc = Calculator()
        numb = 2
        self.assertEqual(calc.llToPercentForHct(numb), 200)

    def test_mgDlToMmolForBUN(self):
        calc = Calculator()
        numb = 2
        self.assertEqual(calc.mgDlToMmolForBUN(numb), 7.14)

    def test_mmolToMgDlForBUN(self):
        calc = Calculator()
        numb = 2
        self.assertAlmostEqual(calc.mmolToMgDlForBUN(numb), 0.56)

    def test_mgDlToMicroMmolForCr(self):
        calc = Calculator()
        numb = 2
        self.assertEqual(calc.mgDlToMicroMmolForCr(numb), 176.8)

    def test_microMmolToMgDlForCr(self):
        calc = Calculator()
        numb = 2
        self.assertEqual(calc.microMmolToMgDlForCr(numb), 0.02)

    def test_mgDlToMicroMmolForBILT(self):
        calc = Calculator()
        numb = 2
        self.assertEqual(calc.mgDlToMicroMmolForBILT(numb), 34.2)

    def test_microMmolToMgDlForBILT(self):
        calc = Calculator()
        numb = 2
        self.assertEqual(round(calc.microMmolToMgDlForBILT(numb), 2), 0.12)

    def test_ngMlToNmolForT3(self):
        calc = Calculator()
        numb = 2
        self.assertEqual(calc.ngMlToNmolForT3(numb), 3.08)

    def test_nmolToNgMlForT3(self):
        calc = Calculator()
        numb = 2
        self.assertEqual(calc.nmolToNgMlForT3(numb), 1.3)

    def test_microGdLToNmolForT4(self):
        calc = Calculator()
        numb = 2
        self.assertEqual(calc.microGdLToNmolForT4(numb), 25.8)

    def test_nmolToMicroGdlForT4(self):
        calc = Calculator()
        numb = 2
        self.assertEqual(calc.nmolToMicroGdlForT4(numb), 0.16)

    def test_ngMltoNmol(self):
        calc = Calculator()
        numb = 2
        self.assertEqual(calc.ngMltoNmol(numb), 5)

    def test_NmolToNgMl(self):
        calc = Calculator()
        numb = 2
        self.assertEqual(calc.NmolToNgMl(numb), 0.8)

    def test_mgDlToMmolForChol(self):
        calc = Calculator()
        numb = 2
        self.assertEqual(calc.mgDlToMmolForChol(numb), 0.0518)

    def test_mmolToMgDlForChol(self):
        calc = Calculator()
        numb = 2
        self.assertEqual(calc.mmolToMgDlForChol(numb), 77.22)

    def test_mgDlToMmolForTG(self):
        calc = Calculator()
        numb = 2
        self.assertEqual(calc.mgDlToMmolForTG(numb), 0.0226)

    def test_mmolToMgDlForTG(self):
        calc = Calculator()
        numb = 2
        self.assertEqual(calc.mmolToMgDlForTG(numb), 176.99)
