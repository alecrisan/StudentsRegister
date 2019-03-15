'''
Created on Nov 12, 2017

@author: Ale
'''
from RepositoryException import *
from Assignment0507.domain.Discipline import *

class DisciplineList:
    def __init__(self):
        self.disciplinesList = list()
        
    def add(self, discipline):
        """
        Adds a discipline to the list
        input: the discipline we want to add
        output: None
        """
        if self.findDById(discipline.getId()) is None:
            self.disciplinesList.append(discipline)
        else:
            raise RepoException("A discipline with the same id already exists")
        
    def removeDisc(self, discipline):
        """
        Removes the discipline with a given ID
        input: the discipline's ID
        output: None
        """
        try:
            self.disciplinesList.remove(discipline)
        except ValueError as e:
            print(e)
    
    def update(self, olddisciplineId, newDiscipline):
        """
        Updates the discipline with a given ID
        input: the old discipline's ID, the new discipline
        output: None
        """
        for index, discipline in enumerate(self.disciplinesList):
            if discipline.getId() == olddisciplineId:
                self.disciplinesList[index] = newDiscipline
                break
            
    def getAll(self):
        """
        Returns all the data from the list
        output: the list of disciplines
        """
        return self.disciplinesList
    
    def printAll(self):
        """
        Prints all the disciplines from the list
        input: -
        output: None
        """
        for discipline in self.disciplinesList:
            print(str(discipline))
    
    def findDById(self, disciplineId):
        """
        Finds a discipline with the given ID
        input: the discipline's ID
        output: the discipline found
        """
        for discipline in self.disciplinesList:
            if discipline.getId() == disciplineId:
                return discipline
    
    def getDName(self, disciplineId):
        """
        Finds the discipline's name by its ID
        input: the discipline's ID
        output: the discipline's Name
        """
        for discipline in self.disciplinesList:
            if discipline.getId() == disciplineId:
                return discipline.getName()
            
    def searchDByName(self, name):
        """
        Search disciplines by a name given
        input: name
        output: True if there was at least one discipline found
                False otherwise
        """
        ok = 0
        for d in self.disciplinesList:
            if d.getName().lower().find(name.lower()) != -1:
                print("Id: " + str(d.getId()) + " Name: " + d.getName())
                ok = 1
        if ok == 1:
            return True
        return False
        
    def searchDById(self, disciplineId):
        """
        Search disciplines by an ID given
        input: id
        output: True if there was at least one discipline found
                False otherwise
        """
        ok = 0
        for d in self.disciplinesList:
            if str(d.getId()).find(str(disciplineId)) != -1:
                print("Id: " + str(d.getId()) + " Name: " + d.getName())
                ok = 1
        if ok == 1:
            return True
        return False
