'''
Created on Nov 15, 2017

@author: Ale
'''
class Grade:
    def __init__(self, studentId, disciplineId, grade_value = "none"):
        self.disciplineId = disciplineId
        self.studentId = studentId
        self.grade_value = grade_value
    
    def __str__(self):
        """
        Overriding the str method
        output: a new string
        """
        return ("Student ID: " + str(self.studentId) + " Discipline ID: " + str(self.disciplineId) + 
        " Grade: " + str(self.grade_value))
        
    def __getitem__(self, index):
        """
        Provides support for the use of square bracket indexing
        input: index
        output: grade[index]
        """
        self.grade = (self.studentId, self.disciplineId, self.grade_value)
        return self.grade[index]
    
    def getStId(self):
        """
        Gets the student's ID
        output: studentId
        """
        return self.studentId
    
    def getDiscId(self):
        """
        Gets the discipline's ID
        output: disciplineId
        """
        return self.disciplineId
    
    def getGrValue(self):
        """
        Gets the grade's value
        output: grade_value
        """
        return self.grade_value
    
    def toString(self):
        """
        Method for the CSV file
        output: a new string
        """
        return str(self.getStId()) + "," + str(self.getDiscId()) + ","  + str(self.getGrValue())
    
        