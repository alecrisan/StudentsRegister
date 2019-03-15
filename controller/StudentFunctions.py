'''
Created on Nov 5, 2017

@author: Ale
'''
from Assignment0507.controller.UndoController import *

class StudentFunct:
    def __init__(self, studentsList, undoController, gradeFunctions):
        self.studentsList = studentsList
        self.undoController = undoController
        self.gradeFunctions = gradeFunctions
        
    def addStudent(self, student, recordForUndo = True):
        """
        Adds a student to the list
        input: the student we want to add
        output: None
        """
        self.studentsList.add(student)
        """
        If the operation did not raise an Exception, then we record it for Undo/Redo
        """
        if recordForUndo == True:
            undo = FunctionCall(self.removeStudent, student.getId(), False)
            redo = FunctionCall(self.addStudent, student, False)
            casOP = CascadedOperation(Operation(redo, undo))
            self.undoController.recordOperation(casOP)
        
    def removeStudent(self, studentId, recordForUndo=True):
        """
        Removes the student with a given ID
        input: the student's ID
        output: None
        """
        student = self.findStudent(studentId)
        self.studentsList.removeSt(student)

        '''
        If the operation did not raise an Exception, then we record it for Undo/Redo
        '''
        grades = self.gradeFunctions.filterGr(student, None)
        
        if recordForUndo == True:
            casOP = CascadedOperation()
            undo = FunctionCall(self.addStudent, student, False)
            redo = FunctionCall(self.removeStudent, studentId, False)
            casOP.add(Operation(redo, undo))
            
            for grade in grades:
                undo = FunctionCall(self.gradeFunctions.addGrade, grade, False)
                redo = FunctionCall(self.gradeFunctions.removeGradesForStudent, studentId, False)
                casOP.add(Operation(redo, undo))
            
            self.undoController.recordOperation(casOP)
            
    def updateStudent(self, oldstudentId, newStudent, recordForUndo=True):
        """
        Updates the student with a given ID
        input: the old student's ID, the new student
        output: None
        """
        oldStudent = self.findStudent(oldstudentId)
        self.studentsList.update(oldstudentId, newStudent)
            
        """
        If the operation did not raise an Exception, then we record it for Undo/Redo
        """
        grades = self.gradeFunctions.filterGr(oldStudent, None)
        
        if recordForUndo == True:
            casOP = CascadedOperation()
            undo = FunctionCall(self.updateStudent, newStudent.getId(), oldStudent, False)
            redo = FunctionCall(self.updateStudent, oldstudentId, newStudent, False)
            casOP.add(Operation(redo, undo))
            
            for grade in grades:
                undo = FunctionCall(self.gradeFunctions.addGrade, grade, False)
                redo = FunctionCall(self.gradeFunctions.removeGradesForStudent, oldstudentId, False)
                casOP.add(Operation(redo, undo))
                
            self.undoController.recordOperation(casOP)
            
    def printList(self):
        """
        Prints all the students from the list
        input: -
        output: None
        """
        self.studentsList.printAll()
            
    def findStudent(self, studentId):
        """
        Finds a student with the given ID
        input: the student's ID
        output: the student found
        """
        student = self.studentsList.findSById(studentId)
        return student
            
    def getStudentName(self, studentId):
        """
        Finds the student's name by his ID
        input: the student's ID
        output: the student's Name
        """
        name = self.studentsList.getSName(studentId)
        return name
            
    def searchStudentByName(self, name):
        """
        Search students by a name given
        input: name
        output: True if there was at least one student found
                False otherwise
        """
        match = self.studentsList.searchStByName(name)
        return match
        
    def searchStudentById(self, studentId):
        """
        Search students by an ID given
        input: id
        output: True if there was at least one student found
                False otherwise
        """
        match = self.studentsList.searchStById(studentId)
        return match   
        
        
        