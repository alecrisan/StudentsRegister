'''
Created on Dec 10, 2017

@author: Ale
'''
from Assignment0507.repository.StudentRepo import StudentList
from Assignment0507.domain.Student import *
from Assignment0507.repository.RepositoryException import *
import pickle

class BinaryStudentList(StudentList):
    def __init__(self, fn):
        StudentList.__init__(self)
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
            self.studentsList = list

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

            pickle.dump(self.studentsList, file)
            file.close()
        except IOError as e:
            raise RepoException(e)
        
    def add(self, student):
        """
        Adds a student to the list
        input: the student we want to add
        output: None
        """
        StudentList.add(self, student)
        self.writeToFile()
        
    def removeSt(self, student):
        """
        Removes the student with a given ID
        input: the student's ID
        output: None
        """
        StudentList.removeSt(self, student)
        self.writeToFile()
        
    def update(self, oldstudentId, newStudent):
        """
        Updates the student with a given ID
        input: the old student's ID, the new student
        output: None
        """
        StudentList.update(self, oldstudentId, newStudent)
        self.writeToFile()
        
    def getAll(self):
        """
        Returns all the data from the list
        output: the list of students
        """
        return StudentList.getAll(self)
    
    def printAll(self):
        """
        Prints all the students from the list
        input: -
        output: None
        """
        StudentList.printAll(self)
        
    def findSById(self, studentId):
        """
        Finds a student with the given ID
        input: the student's ID
        output: the student found
        """
        return StudentList.findSById(self, studentId)
    
    def getSName(self, studentId):
        """
        Finds the student's name by his ID
        input: the student's ID
        output: the student's Name
        """
        return StudentList.getSName(self, studentId)
    
    def searchStById(self, studentId):
        """
        Search students by a name given
        input: name
        output: True if there was at least one student found
                False otherwise
        """
        return StudentList.searchStById(self, studentId)
    
    def searchStByName(self, name):
        """
        Search students by an ID given
        input: id
        output: True if there was at least one student found
                False otherwise
        """
        return StudentList.searchStByName(self, name) 
    