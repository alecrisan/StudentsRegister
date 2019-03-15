'''
Created on Nov 5, 2017

@author: Ale
'''
from Assignment0507.controller.UndoController import *

class DisciplineFunct:
    def __init__(self, disciplinesList, undoController, gradeFunctions):
        self.disciplinesList = disciplinesList
        self.undoController = undoController
        self.gradeFunctions = gradeFunctions
        
    def addDiscipline(self, discipline, recordForUndo=True):
        """
        Adds a discipline to the list
        input: the discipline we want to add
        output: None
        """
        self.disciplinesList.add(discipline)
        
        """
        If the operation did not raise an Exception, then we record it for Undo/Redo
        """
        if recordForUndo == True:
            undo = FunctionCall(self.removeDiscipline, discipline.getId(), False)
            redo = FunctionCall(self.addDiscipline, discipline, False)
            casOP = CascadedOperation(Operation(redo, undo))
            self.undoController.recordOperation(casOP)
        
    def removeDiscipline(self, disciplineId, recordForUndo=True):
        """
        Removes the discipline with a given ID
        input: the discipline's ID
        output: None
        """
        discipline = self.findDiscipline(disciplineId)
        self.disciplinesList.removeDisc(discipline)
        
        '''
        If the operation did not raise an Exception, then we record it for Undo/Redo
        '''
        grades = self.gradeFunctions.filterGr(None, discipline)
        
        if recordForUndo == True:
            casOP = CascadedOperation()
            undo = FunctionCall(self.addDiscipline, discipline, False)
            redo = FunctionCall(self.removeDiscipline, disciplineId, False)
            casOP.add(Operation(redo, undo))
            
            for grade in grades:
                undo = FunctionCall(self.gradeFunctions.addGrade, grade, False)
                redo = FunctionCall(self.gradeFunctions.removeGradesForDiscipline, disciplineId, False)
                casOP.add(Operation(redo, undo))
            
            self.undoController.recordOperation(casOP)
    
    def updateDiscipline(self, olddisciplineId, newDiscipline, recordForUndo=True):
        """
        Updates the discipline with a given ID
        input: the old discipline's ID, the new discipline
        output: None
        """
        oldDiscipline = self.findDiscipline(olddisciplineId)
        self.disciplinesList.update(olddisciplineId, newDiscipline)
        
        """
        If the operation did not raise an Exception, then we record it for Undo/Redo
        """
        grades = self.gradeFunctions.filterGr(None, oldDiscipline)
        
        if recordForUndo == True:
            casOP = CascadedOperation()
            undo = FunctionCall(self.updateDiscipline, newDiscipline.getId(), oldDiscipline, False)
            redo = FunctionCall(self.updateDiscipline, olddisciplineId, newDiscipline, False)
            casOP.add(Operation(redo, undo))
            
            for grade in grades:
                undo = FunctionCall(self.gradeFunctions.addGrade, grade, False)
                redo = FunctionCall(self.gradeFunctions.removeGradesForDiscipline, olddisciplineId, False)
                casOP.add(Operation(redo, undo))
                
            self.undoController.recordOperation(casOP)
    
    def printList(self):
        """
        Prints all the disciplines from the list
        input: -
        output: None
        """
        self.disciplinesList.printAll()
    
    def findDiscipline(self, disciplineId):
        """
        Finds a discipline with the given ID
        input: the discipline's ID
        output: the discipline found
        """
        discipline = self.disciplinesList.findDById(disciplineId)
        return discipline
    
    def getDisciplineName(self, disciplineId):
        """
        Finds the discipline's name by its ID
        input: the discipline's ID
        output: the discipline's Name
        """
        name = self.disciplinesList.getDName(disciplineId)
        return name
    
    def searchDisciplineByName(self, name):
        """
        Search disciplines by a name given
        input: name
        output: True if there was at least one discipline found
                False otherwise
        """
        match = self.disciplinesList.searchDByName(name)
        return match
        
    def searchDisciplineById(self, disciplineId):
        """
        Search disciplines by an ID given
        input: id
        output: True if there was at least one discipline found
                False otherwise
        """
        match = self.disciplinesList.searchDById(disciplineId)
        return match