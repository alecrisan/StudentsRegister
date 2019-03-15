'''
Created on Dec 8, 2017

@author: Ale
'''
from Assignment0507.repository.DisciplineRepo import DisciplineList
from Assignment0507.domain.Discipline import *
from Assignment0507.repository.RepositoryException import *

class CSVDisciplineList(DisciplineList):
    def __init__(self, fn):
        DisciplineList.__init__(self)
        self.filename = fn
        self.loadFromFile()
        
    def loadFromFile(self):
        """
        Loads the data from the file
        output: None
        """
        try:
            file = open(self.filename, "r")
        
            for line in file:
                attributes = line.split(",")
            
                if len(attributes) != 2:
                    continue
                discipline = Discipline(attributes[0].strip(), attributes[1].strip())
            
                self.disciplinesList.append(discipline)
        
            file.close()
        except IOError as e:
            raise RepoException(str(e))
        
    def writeToFile(self):
        """
        Writes the list to the file
        output: None
        """
        try:
            file = open(self.filename, "w")
            for discipline in self.disciplinesList:
                file.write(discipline.toString() + "\n")
            file.close()
        except IOError as e:
            raise RepoException(str(e))
        
    def add(self, discipline):
        """
        Adds a discipline to the list
        input: the discipline we want to add
        output: None
        """
        DisciplineList.add(self, discipline)
        self.writeToFile()
        
    def removeDisc(self, discipline):
        """
        Removes the discipline with a given ID
        input: the discipline's ID
        output: None
        """
        DisciplineList.removeDisc(self, discipline)
        self.writeToFile()
        
    def update(self, olddisciplineId, newDiscipline):
        """
        Updates the discipline with a given ID
        input: the old discipline's ID, the new discipline
        output: None
        """
        DisciplineList.update(self, olddisciplineId, newDiscipline)
        self.writeToFile()
        
    def getAll(self):
        """
        Returns all the data from the list
        output: the list of disciplines
        """
        return DisciplineList.getAll(self)
    
    def printAll(self):
        """
        Prints all the disciplines from the list
        input: -
        output: None
        """
        DisciplineList.printAll(self)
        
    def findDById(self, disciplineId):
        """
        Finds a discipline with the given ID
        input: the discipline's ID
        output: the discipline found
        """
        return DisciplineList.findDById(self, disciplineId)
    
    def getDName(self, disciplineId):
        """
        Finds the discipline's name by its ID
        input: the discipline's ID
        output: the discipline's Name
        """
        return DisciplineList.getDName(self, disciplineId)
    
    def searchDById(self, disciplineId):
        """
        Search disciplines by an ID given
        input: id
        output: True if there was at least one discipline found
                False otherwise
        """
        return DisciplineList.searchDById(self, disciplineId)
    
    def searchDByName(self, name):
        """
        Search disciplines by a name given
        input: name
        output: True if there was at least one discipline found
                False otherwise
        """
        return DisciplineList.searchDByName(self, name)   
