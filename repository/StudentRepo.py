'''
Created on Nov 12, 2017

@author: Ale
'''

from RepositoryException import *
from Assignment0507.domain.Student import *

class StudentList:
    def __init__(self):
        self.studentsList = list()
        
    def add(self, student):
        """
        Adds a student to the list
        input: the student we want to add
        output: None
        """
        if self.findSById(student.getId()) is None:
            self.studentsList.append(student)
        else:
            raise RepoException("Student with the same ID already exists")
        
    def removeSt(self, student):
        """
        Removes the student with a given ID
        input: the student's ID
        output: None
        """
        try:
            self.studentsList.remove(student)
        except ValueError as e:
            print(e)
    
    def update(self, oldstudentId, newStudent):
        """
        Updates the student with a given ID
        input: the old student's ID, the new student
        output: None
        """
        for index, student in enumerate(self.studentsList):
            if student.getId() == oldstudentId:
                self.studentsList[index] = newStudent
                break
            
    def getAll(self):
        """
        Returns all the data from the list
        output: the list of students
        """
        return self.studentsList
        
    def printAll(self):
        """
        Prints all the students from the list
        input: -
        output: None
        """
        for student in self.studentsList:
            print(str(student))
            
    def findSById(self, studentId):
        """
        Finds a student with the given ID
        input: the student's ID
        output: the student found
        """
        for student in self.studentsList:
            if student.getId() == studentId:
                return student
            
    def getSName(self, studentId):
        """
        Finds the student's name by his ID
        input: the student's ID
        output: the student's Name
        """
        for student in self.studentsList:
            if student.getId() == studentId:
                return student.getName()
            
    def searchStByName(self, name):
        """
        Search students by a name given
        input: name
        output: True if there was at least one student found
                False otherwise
        """
        ok = 0
        for s in self.studentsList:
            if s.getName().lower().find(name.lower()) != -1:
                print("Id: " + str(s.getId()) + " Name: " + s.getName())
                ok = 1
        if ok == 1:
            return True
        return False
        
    def searchStById(self, studentId):
        """
        Search students by an ID given
        input: id
        output: True if there was at least one student found
                False otherwise
        """
        ok = 0
        for s in self.studentsList:
            if str(s.getId()).find(str(studentId)) != -1:
                print("Id: " + str(s.getId()) + " Name: " + s.getName())
                ok = 1
        if ok == 1:
            return True
        return False
        
        
