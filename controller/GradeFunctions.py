'''
Created on Nov 5, 2017

@author: Ale
'''
from Assignment0507.controller import StudentFunctions
from Assignment0507.controller import DisciplineFunctions
from Assignment0507.repository import StudentRepo
from Assignment0507.repository import DisciplineRepo
from Assignment0507.controller.UndoController import *
from Assignment0507.domain.Grade import *

class GradeFunct:
    def __init__(self, gradesList, undoController):
        self.gradesList = gradesList
        self.undoController = undoController
    
    def lenn(self, gradesList):
        """
        Overrides the len method
        input: a list
        output: the length of the given list
        """
        length = self.gradesList.__len__(self.gradesList)
        return length
        
    def addGrade(self, grade, recordForUndo=True):
        """
        Adds a grade to the list
        input: the tuple 'grade' which consists of studentId, 
        disciplineId and grade_value
        output: None
        """
        self.gradesList.add(grade)
        
        """
        If the operation did not raise an Exception, then we record it for Undo/Redo
        """
        
        if recordForUndo == True:
            undo = FunctionCall(self.removeGrade, grade, False)
            redo = FunctionCall(self.addGrade, grade, False)
            casOP = CascadedOperation(Operation(redo, undo))
            self.undoController.recordOperation(casOP)
        
    def removeGrade(self, grade, recordForUndo=True):
        """
        Removes a grade from the list
        input: the tuple 'grade' which consists of studentId, 
        disciplineId and grade_value
        output: None
        """
        self.gradesList.removeGr(grade)
    
    def removeGradesForStudent(self, studentId, recordForUndo=True):
        """
        Removes the grades for a given student
        input: the student's ID
        output: None
        """
        self.gradesList.removeGrForSt(studentId)
                
    def removeGradesForDiscipline(self, disciplineId, recordForUndo=True):
        """
        Removes the grades for a given discipline
        input: the discipline's ID
        output: None
        """
        self.gradesList.removeGrForD(disciplineId)
            
    def printList(self, disciplineFunctions, studentFunctions):
        """
        Prints all the grades from the list
        input: -
        output: None
        """
        self.gradesList.printAll(disciplineFunctions, studentFunctions)
            
    def findGradeByStudent(self, studentId):
        """
        Finds a student's grade by his ID
        input: the student's ID
        output: his grade
        """
        grade = self.gradesList.findGrBySt(studentId)
        return grade
    
    def findGradeByDiscipline(self, disciplineId):
        """
        Finds the grade at a discipline by its ID
        input: the discipline's ID
        output: grade
        """
        grade = self.gradesList.findGrByD(disciplineId)
        return grade
            
    def checkGrade(self, grade_value):
        """
        Checks if the grade is between 1 and 10
        input: the grade entered by the user
        output: if the grade is valid, it is returned
                otherwise, it returns None
        """
        gradevalue = self.gradesList.checkGr(grade_value)
        return gradevalue
        
    def enrollStudent(self, grade, recordForUndo=True):
        """
        Enrolls a student with a given ID at a discipline with a given ID
        Since this is only enrolling, not grading, the grade value is initialized with none
        input: a Grade consisting of student's ID, discipline's ID, the grade
        output: None
        """
        self.gradesList.enroll(grade)
        """
        If the operation did not raise an Exception, then we record it for Undo/Redo
        """
        
        if recordForUndo == True:
            undo = FunctionCall(self.removeGrade, grade, False)
            redo = FunctionCall(self.enrollStudent, grade, False)
            casOP = CascadedOperation(Operation(redo, undo))
            self.undoController.recordOperation(casOP)
        
    def checkIfEnrolled(self, studentId, disciplineId):
        """
        Checks if a student with a given ID is enrolled at a discipline with a given ID
        input: student's ID, discipline's ID
        output: if so, the item found is returned
                otherwise, it returns None
        """
        item = self.gradesList.checkIfEnr(studentId, disciplineId)
        return item
            
    
    def statistics1(self, disciplineId):
        """
        Statistics 1
        All students enrolled at a given discipline,sorted by descending order
        of average grade
        input: the given discipline's id
        output: None (it prints out the result to the console)
        """
        lst = self.gradesList.allStEnrolled(disciplineId)
        return lst
        
    def statistics2(self):
        """
        Statistics 2
        All students that are failing at one or more disciplines
        input: -
        output: None (it prints out the result to the console)
        """
        lst = self.gradesList.allStFailing()
        return lst          
                
    def statistics3(self):
        """
        Statistics 3
        Students with the best school situation, sorted by descending order
        of aggregated average grade
        input: -
        output: None (it prints out the result to the console)
        """
        lst = self.gradesList.bestSchoolSituation()
        return lst
    
    def statistics4(self):
        """
        Statistics 4
        Disciplines with at least one grade, sorted by descending order
        of average grade
        input: -
        output: None (it prints out the result to the console)
        """
        lst = self.gradesList.allDisciplines()
        return lst
    
    def filterGr(self, student, discipline):
        """
        Return a list of grades for the given student at the given discipline
        input:
        student (None means all students)
        discipline (None means all disciplines)
        output: list of grades
        """
        lst = self.gradesList.filterGrades(student, discipline)
        return lst
    







    