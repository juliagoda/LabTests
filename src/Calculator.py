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

# Information of units taken from:
# https://erhlin.cch.org.tw/LabSearch/data/SI%20UNIT.PDF
# https://www.amamanualofstyle.com/page/si-conversion-calculator
# http://unitslab.com/node/9

class Calculator():
    
    def __init__(self, parent=None):
        super(Calculator, self).__init__(parent)
        
    # for g/L to g/dL
    # for g/L to g/100mL
    # for pg/ml to ng/dl
    # g/L == mg/mL
    # g/dL == g/100mL
    def divByTen(numb, self):
        return numb / 10
    
    # for g/dL to g/L
    # for g/100mL to g/L
    # for g/L to g/L/10
    # for ng/dl to pg/ml
    def multByTen(numb, self):
        return numb * 10
    
    # for g/L/10 to g/dL
    # for g/L/10 to g/100mL 
    # for ng/dl to ng/ml
    def divBy100(numb, self):
        return numb / 100    
    
    # for g/dL to g/L/10
    # for g/100mL to g/L/10
    # for ng/ml to ng/dl
    def multBy100(numb, self):
        return numb * 100
    
    # for ng/mL to pg/mL
    # for mg/dl to µg/dL
    # for mmol/L to pmol/L
    # for mg/dl to mcg/dl
    def multBy1000(numb, self):
        return numb * 1000
    
    # for pg/mL to ng/mL
    # for µg/dL to mg/dl
    # for pmol/L to mmol/L
    # for mcg/dl to mg/dl
    def divBy1000(numb, self):
        return numb / 1000    
    
    # 10^12 cells/L = T/L = 10^6/µL = 10^6/mm^3 = M/µL = M/mm3
    # for the above equal units to cells/µL 
    def multBy1000000(numb, self):
        return numb * 1000000
    
    # 10^12 cells/L = T/L = 10^6/µL = 10^6/mm^3 = M/µL = M/mm3
    # for cells/µL to the above equal units 
    def divBy1000000(numb, self):
        return numb / 1000000
    
    # g/dL to mmol/L for Hemoglobin
    def gdlToMmolForHgb(numb, self):
        return numb * 0.155
    
    # mmol/L to g/dL for Hemoglobin
    def mmolToGdlForHgb(numb, self):
        return numb / 0.155
    
    # % to L/L for Hematocrit
    def percentToLLForHct(numb, self):
        return numb * 0.01
    
    # L/L to % for Hematocrit
    def llToPercentForHct(numb, self):
        return numb / 0.01
    
    # mg/dL to mmol/L for BUN
    def mgDlToMmolForBUN(numb, self):
        return numb * 0.357 * 10
    
    # mmol/L to mg/dL for BUN
    def mmolToMgDlForBUN(numb, self):
        return numb / 0.357 / 10
        
    # mg/dL to mmol/L for Creatinine
    def mgDlToMicroMmolForCr(numb, self):
        return numb * 88.4
    
    # mmol/L to mg/dL for Creatinine
    def microMmolToMgDlForCr(numb, self):
        return numb / 88.4
    
    # mg/dL to mmol/L for Bil T
    def mgDlToMicroMmolForBILT(numb, self):
        return numb * 17.1
    
    # mmol/L to mg/dL for Bil T
    def microMmolToMgDlForBILT(numb, self):
        return numb / 17.1
    
    # mlU/L = mU/L
    # ng/mL to nmol/L for T3
    def ngMlToNmolForT3(numb, self):
        return numb * 1.54
    
     # nmol/L to ng/mL for T3
    def nmolToNgMlForT3(numb, self):
        return numb / 1.54
    
    # µg/dL to nmol/L for T4
    def microGdLToNmolForT4(numb, self):
        return numb * 12.9
    
    # nmol/L to µg/dL for T4
    def nmolToMicroGdlForT4(numb, self):
        return numb / 12.9
    
    # ng/ml to nmol/L
    def ngMltoNmol(numb, self):
        return numb * 2.5
    
    # nmol/L to ng/ml
    def NmolToNgMl(numb, self):
        return numb / 2.5
    
    # mEq/L = mmol/L
    # mg/dL to mmol/L for Total Cholesterol, LDL and HDL
    def mgDlToMmolForChol(numb, self):
        return numb * 0.0259
    
    # mmol/L to mg/dL for Total Cholesterol, LDL and HDL
    def mmolToMgDlForChol(numb, self):
        return numb / 0.0259
    
    # mg/dL to mmol/L for Triglyceride
    def mgDlToMmolForTG(numb, self):
        return numb * 0.0113
    
    # mmol/L to mg/dL for Triglyceride
    def mmolToMgDlForTG(numb, self):
        return numb / 0.0113

