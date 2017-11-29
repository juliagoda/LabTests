# -*- coding: utf-8 -*-

import yaml
import os
from decimal import Decimal
from PyQt5.QtWidgets import QMessageBox


class Summary:
    
    __resultsDict = {}
    __listForLacks = {}
    
    def __init__(self, allYourTestsDict, personDict):
        
        print([["[ " + key1 + " ][ " + key2 + " ] = " + value2 
                for key2, value2 in value1.items()]
                for key1, value1 in allYourTestsDict.items()])
        cleanDict = self.__removeEmptyListsFromList(allYourTestsDict)
        print("cleaning...")
        print([["[ " + key1 + " ][ " + key2 + " ] = " + value2 
                for key2, value2 in value1.items()]
                for key1, value1 in cleanDict.items()])
        
        if (not self.__checkIfMainListEmpty(cleanDict)):
            if (self.__atLeastBloodDict(cleanDict)):
                self.__getContentForOldDict(cleanDict, personDict, "Blood", "sources/bloodResults.yaml")
        
        if (not self.__checkIfMainListEmpty(cleanDict)):
            if (self.__atLeastUrineDict(cleanDict)):
                self.__getContentForOldDict(cleanDict, personDict, "Urine", "sources/urineResults.yaml")
                
        if (not self.__checkIfMainListEmpty(cleanDict)):
            if (self.__atLeastLiverDict(cleanDict)):
                self.__getContentForOldDict(cleanDict, personDict, "Liver", "sources/liverResults.yaml")

        
        self.getResultsDictLen()
        self.showAllDescDictElemKey()
        
        pass
    
    def getResultsDict(self):
        return self.__resultsDict
    
    def getListOfLacks(self):
        return self.__listForLacks
    
    def clearListOfLacks(self):
        return self.__listForLacks.clear()
    
    def getResultsDictLen(self):
        print ("length of dictionary with descriptions: " + str(len(self.__resultsDict)))
        return len(self.__resultsDict)
    
    def showAllDescDictElemKey(self):
        print(["[ " + key1 + " ] = " + value1
                for key1, value1 in self.__resultsDict.items()])
    
    # gets rid of everything that is "falsy", e.g. empty strings, empty tuples, zeros
    def __removeEmptyListsFromList(self, listOrig): 
        list2 = {}
        for k, v in listOrig.items():
            if v:
                for k2, v2 in v.items():
                     if (v2 and not str(v2).isspace()): 
                         list2[k] = v 
        return list2
    
    def __checkIfMainListEmpty(self, listAfter):
        if not listAfter:
            print("List in Summary class is EMPTY")
            return True
        else:
            print("List in Summary class is NOT EMPTY")
            return False
    
    #if there are "Blood-Morphology", "Blood-WCC" or "Blood-Bio" keys in main dictionary
    def __atLeastBloodDict(self, oldDict):
        if any(key in oldDict for key in ['Blood-Morphology', 'Blood-WCC', 'Blood-Bio']):
            return True
        else:
            return False
        
        #if there are "Urine-Bio",or "Urine-General" keys in main dictionary
    def __atLeastUrineDict(self, oldDict):
        if any(key in oldDict for key in ['Urine-Bio', 'Urine-General']):
            return True
        else:
            return False
        
            #if there are "Liver-Test" keys in main dictionary
    def __atLeastLiverDict(self, oldDict):
        if any(key in oldDict for key in ['Liver-Test']):
            return True
        else:
            return False
        
    def __getOrganYamlFileContent(self, filepath):   
        if(os.stat(filepath).st_size != 0):
            with open(filepath,"r") as organYamlContent:
                organContent = yaml.safe_load(organYamlContent)
                return organContent 
        else:
            print(filepath + " file is detected as empty")
            return
        
    def __getPrefixOfMeasurement(self, elemString):
        return elemString.split(None, 1)[-1]
    
    def __getValueOfMeasurement(self, elemString):
        return elemString.split(None, 1)[0]
    
    def __getPrefixOfYearKey(self, elemString):
        return elemString.split('-', 1)[-1]
        
    def __getContentForOldDict(self, oldDict, personDict, organ, file):
        self.clearListOfLacks()
        if (self.__atLeastBloodDict(oldDict)):
            bloodYamlContent = self.__getOrganYamlFileContent(file)
            bloodTestItems = bloodYamlContent.get('Test')
            for key1, value1 in oldDict.items():
                if organ in key1: # checks substring "Blood" in dictionary key
                    for key2, value2 in value1.items():
                        measurement = self.__getPrefixOfMeasurement(value2)
                        gender = personDict.get('Gender')
                        i = 0
                        for k, v in personDict.items():
                            if (i == 1):
                               prefixYear = self.__getPrefixOfYearKey(k) 
                               age = v
                            i = i + 1
                        if key1 in bloodTestItems:
                            if key2 in bloodTestItems[key1]:
                                if measurement in bloodTestItems[key1][key2]:
                                    pathToRange = bloodTestItems[key1][key2][measurement][gender]['Age'][prefixYear]['RangeMin']
                                    for minRange in pathToRange.keys():        
                                        if (age >= minRange):
                                            for maxRange in pathToRange[minRange]['RangeMax']:
                                                if (age <= maxRange):
                                                    pathToCells = pathToRange[minRange]['RangeMax'][maxRange]['CellsMin']
                                                    for minCellCount in pathToCells:
                                                        if (Decimal(self.__getValueOfMeasurement(value2)) >= minCellCount):
                                                            for maxCellCount in pathToCells[minCellCount]['CellsMax']:  
                                                                if (Decimal(self.__getValueOfMeasurement(value2)) <= maxCellCount):  
                                                                    print("minRange = " + str(minRange))
                                                                    print("maxRange = " + str(maxRange))
                                                                    print("cellsMin = " + str(minCellCount))
                                                                    print("cellsMax = " + str(maxCellCount))
                                                                    print("your age = " + str(age) + " " + str(prefixYear))
                                                                    print("your cells count = " + str(value2))
                                                                    for desc in pathToCells[minCellCount]['CellsMax'][maxCellCount].values():
                                                                        self.__resultsDict[str(key1)] = desc
                                                                        print("description = " + desc)
                                                                    
                                                                else:
                                                                    continue
                                                else:
                                                    continue  
                                else:
                                    self.__listForLacks[organ] = str(measurement)
                            else:
                                self.__listForLacks[organ] = str(key2)
                        else:
                            self.__listForLacks[organ] = str(key1)
       
