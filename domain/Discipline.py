'''
Created on Nov 15, 2017

@author: Ale
'''
class Discipline:
    def __init__(self, disciplineId, disciplineName):
        self.disciplineId = disciplineId
        self.disciplineName = disciplineName
        
    def __str__(self):
        """
        Overriding the str method
        output: a new string
        """
        return "ID: " + str(self.disciplineId) + " Name: " + str(self.disciplineName)
    
    def __getitem__(self, index):
        """
        Provides support for the use of square bracket indexing
        input: index
        output: discipline[index]
        """
        self.discipline = (self.disciplineId, self.disciplineName)
        return self.discipline[index]
    
    def getId(self):
        """
        Gets the discipline's ID
        output: disciplineId
        """
        return self.disciplineId
    
    def getName(self):
        """
        Gets the discipline's name
        output: disciplineName
        """
        return self.disciplineName
    
    def toString(self):
        """
        Method for the CSV file
        output: a new string
        """
        return str(self.getId()) + ","  + str(self.getName())
