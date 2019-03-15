'''
Created on Nov 12, 2017

@author: Ale
'''
from Assignment0507.controller import StudentFunctions
from Assignment0507.controller import DisciplineFunctions
from Assignment0507.repository import StudentRepo
from Assignment0507.repository import DisciplineRepo
from Assignment0507.domain.Grade import *
from Assignment0507.domain.Student import *
from Assignment0507.domain.Discipline import *
import operator

class GradeList:
    def __init__(self):
        self.gradesList = list()
    
    def __len__(self, gradesList):
        """
        Overrides the len method
        input: a list
        output: the length of the given list
        """
        return len(self.gradesList)
        
    def add(self, grade):
        """
        Adds a grade to the list
        input: the tuple 'grade' which consists of studentId, 
        disciplineId and grade_value
        output: None
        """
        self.gradesList.append(grade)
    
    def removeGr(self, grade):
        """
        Removes a grade from the list
        input: the tuple 'grade' which consists of studentId, 
        disciplineId and grade_value
        output: None
        """
        try:
            self.gradesList.remove(grade)
        except ValueError as e:
            print(e)
        
    def removeGrForSt(self, studentId):
        """
        Removes the grades for a given student
        input: the student's ID
        output: None
        """
        try:
            for grade in self.gradesList:
                if grade.getStId() == studentId:
                    self.gradesList.remove(self.findGrBySt(studentId))
        except ValueError as e:
            print(e)
                
    def removeGrForD(self, disciplineId):
        """
        Removes the grades for a given discipline
        input: the discipline's ID
        output: None
        """
        try:
            for grade in self.gradesList:
                if grade.getDiscId() == disciplineId:
                    self.gradesList.remove(self.findGrByD(disciplineId))
        except ValueError as e:
            print(e)
    
    def getAll(self):
        """
        Returns all the data from the list
        output: the list of grades
        """
        return self.gradesList
    
    def printAll(self, disciplineFunctions, studentFunctions):
        """
        Prints all the grades from the list
        input: -
        output: None
        """
        for grade in self.gradesList:
            print("Student: " + str(studentFunctions.getStudentName(grade.getStId())) + " Discipline: " + str(disciplineFunctions.getDisciplineName(grade.getDiscId())) + " Grade:" + 
            str(grade.getGrValue()))
            
    def findGrBySt(self, studentId):
        """
        Finds a student's grade by his ID
        input: the student's ID
        output: his grade
        """
        for grade in self.gradesList:
            if grade.getStId() == studentId:
                return grade
    
    def findGrByD(self, disciplineId):
        """
        Finds the grade at a discipline by its ID
        input: the discipline's ID
        output: grade
        """
        for grade in self.gradesList:
            if grade.getDiscId() == disciplineId:
                return grade
            
    def checkGr(self, grade_value):
        """
        Checks if the grade is between 1 and 10
        input: the grade entered by the user
        output: if the grade is valid, it is returned
                otherwise, it returns None
        """
        if grade_value >=1 and grade_value <= 10:
            return grade_value
        
    def enroll(self, grade):
        """
        Enrolls a student with a given ID at a discipline with a given ID
        Since this is only enrolling, not grading, the grade value is initialized with none
        input: a Grade consisting of student's ID, discipline's ID, the grade
        output: None
        """
        self.add(Grade(grade.getStId(), grade.getDiscId(), grade_value="none"))
        
    def checkIfEnr(self, studentId, disciplineId):
        """
        Checks if a student with a given ID is enrolled at a discipline with a given ID
        input: student's ID, discipline's ID
        output: if so, it returns True
                otherwise, it returns False
        """
        ok = 0
        for item in self.gradesList:
            if item.getStId() == studentId and item.getDiscId() == disciplineId:
                ok = 1
                if item.getGrValue() == "none":
                    self.gradesList.remove(self.findGrByD(disciplineId))
        if ok == 1:
            return True
        return False
        
    def getAvgGrForSt(self, studentId, disciplineId):
        """
        Computes the average grade for a given student at a given discipline
        input: the student's id, the discipline's id
        output: the average grade
                0 if the student doesn't have any grades at that discipline
        """
        nr = 0
        s = 0
        for item in self.gradesList:
            if item.getStId() == studentId and item.getDiscId() == disciplineId and item.getGrValue() != 'none':
                nr = nr + 1
                s = s + float(item.getGrValue())
        if nr != 0:
            return float(s/nr)
        return 0
    
    def getAvgForDisc(self, disciplineId):
        """
        Computes the average for a given discipline
        input: discipline's Id
        output: the average grade
        """
        s = 0
        nr = 0
        for item in self.gradesList:
            if item.getDiscId() == disciplineId and item.getGrValue() != "none":
                nr = nr + 1
                s = s + float(item.getGrValue())
                
        if nr!= 0:
            return float(s/nr)
        return 0
    
    def getAggregatedAvg(self, studentId):
        """
        Computes the aggregated average grade for a student 
        (the average between their average grades per discipline)
        input: the student's id
        output: the aggregated average grade
        """
        nr = 0
        s = 0
        for item in self.gradesList:
            if item.getStId() == studentId:
                avg = self.getAvgGrForSt(item.getStId(), item.getDiscId())
                s = s + float(avg)
                nr = nr + 1
        if nr != 0:
            return float(s/nr)
        return 0
        
    def bestSchoolSituation(self):
        """
        Gets all students that have been graded at least once, along with their aggregated average grade
        input: -
        output: the sorted list
        """
        auxList = []
        auxSt = []
        for item in self.gradesList:
            if self.getAggregatedAvg(item.getStId()) != 0 and item.getStId() not in auxSt:
                auxList.append(BestSchoolSit(item.getStId(), self.getAggregatedAvg(item.getStId())))
                auxSt.append(item.getStId())
        
        for i in range(0, len(auxList) - 1):
            for j in range(i + 1, len(auxList)):
                if auxList[i].getAvg() < auxList[j].getAvg():
                    auxList[i], auxList[j] = auxList[j], auxList[i]
        
        return auxList
     
    def checkIfFailing(self, studentId, disciplineId):
        """
        checks if a given student is failing at a given discipline
        input: the student's id, the discipline's id
        output: True if failing
                False otherwise
        """
        if self.getAvgGrForSt(studentId, disciplineId) < 5:
            return True
        return False
    
    def allStFailing(self):
        """
        Gets all students that are failing at one or more disciplines
        input: -
        output: the list 
        """
        auxList = []
        for item in self.gradesList:
            if self.checkIfFailing(item.getStId(), item.getDiscId()) == True:
                auxList.append(AllStudents(item.getStId(), item.getDiscId(), self.getAvgGrForSt(item.getStId(), item.getDiscId())))
                
        return auxList
                      
    def allStEnrolled(self, disciplineId):
        """
        Gets all students enrolled at a given discipline, sorted by descending order
        of average grade
        input: the given discipline's id
        output: the sorted list
        """
        auxList = []
        auxSt = []
        for item in self.gradesList:
            if item.getDiscId() == disciplineId and item.getStId() not in auxSt:
                auxList.append(AllStudents(item.getStId(), item.getDiscId(), self.getAvgGrForSt(item.getStId(), item.getDiscId())))
                auxSt.append(item.getStId())
        
        for i in range(0, len(auxList) - 1):
            for j in range(i + 1, len(auxList)):
                if auxList[i].getAvg() < auxList[j].getAvg():
                    auxList[i], auxList[j] = auxList[j], auxList[i]
                    
        return auxList
    
    def allDisciplines(self):
        """
        Gets all disciplines with at least one grade, sorted by descending order
        of average grade
        input: -
        output: the sorted list
        """
        auxList = []
        auxD = []
        for item in self.gradesList:
            if item.getGrValue() != "none" and item.getDiscId() not in auxD:
                auxList.append(AllDisciplines(item.getDiscId(), self.getAvgForDisc(item.getDiscId())))
                auxD.append(item.getDiscId())
        
        for i in range(0, len(auxList) - 1):
            for j in range(i + 1, len(auxList)):
                if auxList[i].getAvg() < auxList[j].getAvg():
                    auxList[i], auxList[j] = auxList[j], auxList[i]
                    
        return auxList
     
    def filterGrades(self, student, discipline):
        """
        Return a list of grades for the given student at the given discipline
        input:
        student (None means all students)
        discipline (None means all disciplines)
        output: list of grades
        """
        result = []
        for grade in self.gradesList:
            if student != None and grade.getStId() != student.getId():
                continue
            if discipline != None and grade.getDiscId() != discipline.getId():
                continue
            result.append(grade)
        return result  
        
class BestSchoolSit():
    def __init__(self, studentId, aggregated_average):
        self.studentId = studentId
        self.aggregated_average = aggregated_average
        
    def getStId(self):
        """
        Gets the student's ID
        output: studentId
        """
        return self.studentId
    
    def getAvg(self):
        """
        Gets the average grade
        output: aggregated_average
        """
        return self.aggregated_average
    
class AllStudents():
    def __init__(self, studentId, disciplineId, average_grade):
        self.studentId = studentId
        self.disciplineId = disciplineId
        self.average_grade = average_grade
        
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
    
    def getAvg(self):
        """
        Gets the average grade
        output: average_grade
        """
        return self.average_grade
    
class AllDisciplines():
    def __init__(self, disciplineId, average_grade):
        self.disciplineId = disciplineId
        self.average_grade = average_grade
        
    def getDiscId(self):
        """
        Gets the discipline's ID
        output: disciplineId
        """
        return self.disciplineId
    
    def getAvg(self):
        """
        Gets the average grade
        output: average_grade
        """
        return self.average_grade
    
    
      
    
      
        
