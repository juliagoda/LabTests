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

# To run this: python -m unittest


import unittest
import sqlalchemy

class TestDB(unittest.TestCase):
    
    __engine = None
    __connection = None
    
    def __init__(self, *args, **kwargs):
        super(TestDB, self).__init__(*args, **kwargs)
        self.__engine = sqlalchemy.create_engine("SOME_ADDRESS") # of course it's not real yet
        self.__connection = self.__engine.connect()
        self.assertFalse(self.__connection.invalidated)
        self.assertFalse(self.__connection.closed)


    def test_hasTableLabs(self):
        self.assertTrue(self.__engine.has_table("labtests"))
        
    def test_hasTableDesc(self):
        self.assertTrue(self.__engine.has_table("targetdesc"))
        
    
    def test_containsAllNeededTests(self):
        
        statement = self.__connection.execute("SELECT * FROM `labtests` WHERE `targetfullname` NOT IN('White Blood Cells','Hemoglobin','Platelets', 'Hematocrit', 'Sodium', 'Potassium', 'Calcium', 'Chloride', 'Phosphate', 'Magnesium', 'Blood Urea Nitrogen', 'Creatinine', 'Glucose', 'Glycohemoglobin', 'Thyroxine', 'Triiodothyronine', 'Thyroid', 'Bicarbonate', 'Arterial carbon dioxide', 'Albumin', 'Prealbumin', 'Bilirubin', 'Ammonia', 'High-Density Lipoprotein', 'Low-Density Lipoprotein', 'Triglycerides', 'Total Cholesterol')").fetchall()
        
        self.assertFalse(statement)
        
        
    # check if in table targetdesc the same column has some different value (comparision to labtests)
    # It's ok when everything is equal (because of reference to relational table)
    def test_containNotEqualTargets(self):
        
        statement = self.__connection.execute("SELECT * FROM `targetdesc` WHERE `targetfullname` NOT IN(SELECT `labtests`.`targetfullname` FROM `labtests`)").fetchall()
        
        if statement:
            for row_number, row in enumerate(statement):
                print("In targetdesc exists other value: ", row["targetfullname"], " at row ", row_number) 
                    
        self.assertFalse(statement)
        
        
    # check if in table labtests the same column has some different value (comparision to targetdesc)
    # It's ok when everything is equal (because of reference to relational table)
    def test_containNotEqualTargetsLabTests(self):
        
        statement = self.__connection.execute("SELECT * FROM `labtests` WHERE `targetfullname` NOT IN(SELECT `targetdesc`.`targetfullname` FROM `targetdesc`)").fetchall()
        
        if statement:
            for row_number, row in enumerate(statement):
                print("In labtests exists other value: ", row["targetfullname"], " at row ", row_number) 
                    
        self.assertFalse(statement)
        
        
      # if table contains duplicated rows
    def test_containsDuplications(self):
        
        statement = self.__connection.execute("SELECT `gender`, `age-range-start`, `age-range-end`, `age-type`, `targetfullname`, count(*) FROM `labtests` GROUP BY `gender`, `age-range-start`, `age-range-end`, `age-type`, `targetfullname` HAVING count(*) > 1").fetchall()
        
        if statement:
            for row_number, row in enumerate(statement):
                print("Duplicated row for ", row["targetfullname"]) 
                    
        self.assertFalse(statement)
        
            
       # if table contains not proper unit
    def test_containsNotProperUnit(self):
        
        statement = self.__connection.execute("SELECT * FROM `labtests` WHERE `unit` NOT IN('fL', 'g', 'g/dL', 'g/L', 'IU/L', 'IU/mL', 'mcg', 'mcg/dL', 'mcg/L', 'mckat/L', 'mcL', 'mcmol/L', 'mEq', 'mEq/L', 'mg', 'mg/dL', 'mg/L', 'mIU/L', 'mL', 'mm', 'mm Hg', 'mmol', 'mmol/L', 'mOsm/kg', 'mU/g', 'mU/L', 'ng/dL', 'ng/L', 'ng/mL', 'ng/mL/hr', 'nmol', 'nmol/L', 'pg', 'pg/mL', 'pmol/L', 'U/L', 'U/mL', 'μU/mL', 'µg/dL', 'µg/L', 'mL/min', 'mL/S', '%%')").fetchall()
        
        self.assertFalse(statement)
        
        
        # if table contains not proper abbreviations for laboratory tests 
    def test_containsNotProperAbbr(self):
        
        statement = self.__connection.execute("SELECT * FROM `targetdesc` WHERE `targetshortname` NOT IN('A1A', 'A1c', 'AB', 'ABG', 'ABRH', 'ABT', 'ACA', 'ACE', 'ACID PHOS', 'ACP', 'ACT', 'ACTH', 'ADA', 'AFB', 'AFP', 'AG', 'ALA', 'Alb', 'Alk Phos', 'ALP', 'ANA', 'Anti-HBc', 'Anti-HBe', 'Anti-HBs', 'Anti-HCV', 'APT', 'aPTT', 'ASN', 'ASO', 'ASP', 'AT III', 'B12', 'BMP', 'BNP', 'BUN', 'C1', 'C1Q', 'C2', 'C3', 'C4', 'Ca', 'CBC', 'CBCD', 'CEA', 'CH50', 'CK', 'Cl ', 'CMB', 'CMP', 'CMV', 'CMV Ag', 'CO', 'CO2', 'COHB', 'CONABO', 'CPK', 'Cr', 'CRCL', 'CrCl', 'CRD', 'CREAT', 'CRP', 'Cu', 'D Bil ', 'DAT', 'DCAS', 'DHEA', 'DHEAS', 'DIFM', 'Dig', 'EOS', 'EPO', 'ERA', 'ESR', 'ETOH', 'FBS', 'Fe', 'FEP', 'FFN', 'FFQ', 'Fol', 'FSH/LH', 'FT3', 'FT4', 'G2PP', 'G-6-PD', 'Gamma GT', 'GCT', 'GDS', 'GGT', 'GH', 'Glu', 'H&H', 'H/H', 'Hapto', 'HbA1c', 'HBeAb', 'HBeAg', 'HBsAb', 'HBsAg', 'hCG', 'hCG (urine)', 'HCT', 'HDL', 'HFP', 'HGB', 'HgbA1c', 'HGH', 'HIAA', 'HIV', 'HPV', 'HSV', 'iCa', 'IFE', 'IgA', 'IgE', 'IGF', 'IgG', 'IgM', 'INR', 'Jo-1', 'KB', 'K', 'Lact(o)', 'LD', 'LDH', 'LFT', 'LH', 'Li+', 'Li', 'MetHb', 'MetHgb', 'Mg', 'Mag', 'MIC', 'MMA', 'Mn', 'Mono', 'NA', 'NEOTY', 'NEOXM', 'NH3', 'NTR', 'PAP', 'Pb', 'PBG', 'PCP', 'PEP', 'PHOS', 'PKU', 'PLT', 'PLT Ct', 'PO4', 'PRL', 'PRU', 'PSA', 'PT', 'PTH', 'PTT', 'QIG', 'RBC', 'RET', 'RF', 'RFP', 'RhIG (Eval)', 'RPR', 'RSV', 'Scl-70', 'SHBG', 'SIFE', 'Siro', 'SPEP', 'SSA', 'SSB', 'SSDNA', 'TBIL/SBR', 'T3', 'T4', 'Tacro', 'TBG', 'TGL', 'Theo', 'TIBC', 'TP', 'TREP', 'Trep Ab', 'TRH', 'Trig', 'TRXN', 'TSH', 'TSI', 'TT', 'TYSC', 'UIFE', 'UPE', 'UPEP', 'Ur Prot Elect', 'VCA', 'VDRL', 'Vit A', 'Vit B1', 'Vit B12', 'Vit B2', 'Vit B6', 'Vit C', 'Vit D', 'VLDL', 'VMA', 'VZG', 'WBC', 'Xa', 'XM', 'Zn', 'ZPP', 'Hb', 'Hgb', 'PaCO2', 'HCO3', 'PA / PAB / PALB', 'LDL', 'TC', 'TG')").fetchall()
        
        self.assertFalse(statement)
        
        
    def test_DBclose(self):
        self.__connection.close()
        self.assertTrue(self.__connection.closed)
