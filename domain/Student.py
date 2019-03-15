'''
Created on Nov 15, 2017

@author: Ale
'''
class Student:
    def __init__(self, studentId, studentName):
        self.studentId = studentId
        self.studentName = studentName
        
    def __str__(self):
        """
        Overriding the str method
        output: a new string
        """
        return "ID: " + str(self.studentId) + " Name: " + str(self.studentName)
    
    def __getitem__(self, index):
        """
        Provides support for the use of square bracket indexing
        input: index
        output: student[index]
        """
        self.student = (self.studentId, self.studentName)
        return self.student[index]
    
    def getId(self):
        """
        Gets the student's ID
        output: studentId
        """
        return self.studentId
    
    def getName(self):
        """
        Gets the student's name
        output: studentName
        """
        return self.studentName
    
    def toString(self):
        """
        Method for the CSV file
        output: a new string
        """
        return str(self.getId()) + ","  + str(self.getName())

