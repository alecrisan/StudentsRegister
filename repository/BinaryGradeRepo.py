'''
Created on Dec 11, 2017

@author: Ale
'''
from Assignment0507.repository.GradeRepo import GradeList
from Assignment0507.domain.Grade import *
from Assignment0507.repository.RepositoryException import *
import pickle

class BinaryGradeList(GradeList):
    def __init__(self, fn):
        GradeList.__init__(self)
        self.filename = fn
        self.loadFromFile()
        
    def loadFromFile(self):
        """
        Loads the data from the file
        output: None
        """
        try:
            file = open(self.filename, "rb")
            list = pickle.load(file)
            self.gradesList = list

            file.close()
        except IOError as e:
            raise RepoException(e)
        except EOFError as p:
            pass

    def writeToFile(self):
        """
        Writes the list to the file
        output: None
        """
        try:
            file = open(self.filename, "wb")

            pickle.dump(self.gradesList, file)
            file.close()
        except IOError as e:
            raise RepoException(e)
        
    def __len__(self, gradesList):
        """
        Overrides the len method
        input: a list
        output: the length of the given list
        """
        return GradeList.__len__(self, gradesList)
    
    def add(self, grade):
        """
        Adds a grade to the list
        input: the tuple 'grade' which consists of studentId, 
        disciplineId and grade_value
        output: None
        """
        GradeList.add(self, grade)
        self.writeToFile()
        
    def removeGr(self, grade):
        """
        Removes a grade from the list
        input: the tuple 'grade' which consists of studentId, 
        disciplineId and grade_value
        output: None
        """
        GradeList.removeGr(self, grade)
        self.writeToFile()
        
    def removeGrForSt(self, studentId):
        """
        Removes the grades for a given student
        input: the student's ID
        output: None
        """
        GradeList.removeGrForSt(self, studentId)
        self.writeToFile()
        
    def removeGrForD(self, disciplineId):
        """
        Removes the grades for a given discipline
        input: the discipline's ID
        output: None
        """
        GradeList.removeGrForD(self, disciplineId)
        self.writeToFile()
        
    def getAll(self):
        """
        Returns all the data from the list
        output: the list of grades
        """
        return GradeList.getAll(self)
    
    def printAll(self, disciplineFunctions, studentFunctions):
        """
        Prints all the grades from the list
        input: -
        output: None
        """
        GradeList.printAll(self, disciplineFunctions, studentFunctions)
        
    def findGrBySt(self, studentId):
        """
        Finds a student's grade by his ID
        input: the student's ID
        output: his grade
        """
        return GradeList.findGrBySt(self, studentId)
    
    def findGrByD(self, disciplineId):
        """
        Finds the grade at a discipline by its ID
        input: the discipline's ID
        output: grade
        """
        return GradeList.findGrByD(self, disciplineId)
    
    def checkGr(self, grade_value):
        """
        Checks if the grade is between 1 and 10
        input: the grade entered by the user
        output: if the grade is valid, it is returned
                otherwise, it returns None
        """
        return GradeList.checkGr(self, grade_value)
    
    def enroll(self, grade):
        """
        Enrolls a student with a given ID at a discipline with a given ID
        Since this is only enrolling, not grading, the grade value is initialized with none
        input: a Grade consisting of student's ID, discipline's ID, the grade
        output: None
        """
        GradeList.enroll(self, grade)
        
    def checkIfEnr(self, studentId, disciplineId):
        """
        Checks if a student with a given ID is enrolled at a discipline with a given ID
        input: student's ID, discipline's ID
        output: if so, it returns True
                otherwise, it returns False
        """
        return GradeList.checkIfEnr(self, studentId, disciplineId)
    
    def getAvgGrForSt(self, studentId, disciplineId):
        """
        Computes the average grade for a given student at a given discipline
        input: the student's id, the discipline's id
        output: the average grade
                0 if the student doesn't have any grades at that discipline
        """
        return GradeList.getAvgGrForSt(self, studentId, disciplineId)
    
    def getAvgForDisc(self, disciplineId):
        """
        Computes the average for a given discipline
        input: discipline's Id
        output: the average grade
        """
        return GradeList.getAvgForDisc(self, disciplineId)
    
    def getAggregatedAvg(self, studentId):
        """
        Computes the aggregated average grade for a student 
        (the average between their average grades per discipline)
        input: the student's id
        output: the aggregated average grade
        """
        return GradeList.getAggregatedAvg(self, studentId)
    
    def bestSchoolSituation(self):
        """
        Gets all students that have been graded at least once, along with their aggregated average grade
        input: -
        output: the sorted list
        """
        return GradeList.bestSchoolSituation(self)
    
    def checkIfFailing(self, studentId, disciplineId):
        """
        checks if a given student is failing at a given discipline
        input: the student's id, the discipline's id
        output: True if failing
                False otherwise
        """
        return GradeList.checkIfFailing(self, studentId, disciplineId)
    
    def allStFailing(self):
        """
        Gets all students that are failing at one or more disciplines
        input: -
        output: the list 
        """
        return GradeList.allStFailing(self)
    
    def allStEnrolled(self, disciplineId):
        """
        Gets all students enrolled at a given discipline, sorted by descending order
        of average grade
        input: the given discipline's id
        output: the sorted list
        """
        return GradeList.allStEnrolled(self, disciplineId)
    
    def allDisciplines(self):
        """
        Gets all disciplines with at least one grade, sorted by descending order
        of average grade
        input: -
        output: the sorted list
        """
        return GradeList.allDisciplines(self)
    
    def filterGrades(self, student, discipline):
        """
        Return a list of grades for the given student at the given discipline
        input:
        student (None means all students)
        discipline (None means all disciplines)
        output: list of grades
        """
        return GradeList.filterGrades(self, student, discipline)