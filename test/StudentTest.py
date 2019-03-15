'''
Created on Nov 7, 2017

@author: Ale
'''
from unittest import TestCase
from Assignment0507.repository.StudentRepo import *
from Assignment0507.domain.Student import *

class TestsStudent(TestCase):
    def testAdd(self):
        studentsList = StudentList()
        
        studentsList.add((Student(1, "Adrian")))
        studentsList.add((Student(5, "Bianca")))
        studentsList.add((Student(9, "Cristi")))
        
        assert studentsList.studentsList[0].getId() == 1
        assert studentsList.studentsList[1].getId() == 5
        assert studentsList.studentsList[2].getId() == 9
        
    def testRemove(self):
        studentsList = StudentList()
        
        studentsList.add(Student(1, "Adrian"))
        studentsList.add(Student(5, "Bianca"))
        studentsList.add(Student(9, "Cristi"))
        
        studentsList.removeSt(Student(5, "Bianca"))
        
        assert studentsList.studentsList[1].getId() == 5
    
    def testUpdate(self):
        studentsList = StudentList()
        
        studentsList.add(Student(1, "Adrian"))
        studentsList.add(Student(9, "Cristi"))
        s3 = Student(5, "Bianca")
        
        
        studentsList.update(9, s3)
        
        assert studentsList.studentsList[1].getId() == 5
        assert studentsList.studentsList[1].getName() == "Bianca"
        
    def testfindSById(self):
        studentsList = StudentList()
        
        s1 = Student(1, "Adrian")
        s2 = Student(5, "Bianca")
        s3 = Student(9, "Cristi")
        
        studentsList.add(s1)
        studentsList.add(s2)
        studentsList.add(s3)
        
        assert studentsList.findSById(1) == s1
        assert studentsList.findSById(5) == s2
        assert studentsList.findSById(9) == s3
        assert studentsList.findSById(2) is None
        
    def testgetSName(self):
        studentsList = StudentList()
        
        s1 = Student(1, "Adrian")
        s2 = Student(5, "Bianca")
        s3 = Student(9, "Cristi")
        
        studentsList.add(s1)
        studentsList.add(s2)
        studentsList.add(s3)
        
        assert studentsList.getSName(1) == "Adrian"
        assert studentsList.getSName(5) == "Bianca"
        assert studentsList.getSName(9) == "Cristi"
        assert studentsList.getSName(2) is None
        
    def testgetId(self):
        s1 = Student(1, "Adrian")
        s2 = Student(5, "Bianca")
        s3 = Student(9, "Cristi")
        
        assert s1.getId() == 1
        assert s2.getId() == 5
        assert s3.getId() == 9
        
    def testgetName(self):
        s1 = Student(1, "Adrian")
        s2 = Student(5, "Bianca")
        s3 = Student(9, "Cristi")
        
        assert s1.getName() == "Adrian"
        assert s2.getName() == "Bianca"
        assert s3.getName() == "Cristi"
        
    def testsearchStByName(self):
        studentsList = StudentList()
        
        s1 = Student(1, "Adrian")
        s2 = Student(5, "Bianca")
        s3 = Student(9, "Cristi")
        
        studentsList.add(s1)
        studentsList.add(s2)
        studentsList.add(s3)
        
        assert studentsList.searchStByName("Bianca") == True
        assert studentsList.searchStByName("SS") == False
        assert studentsList.searchStByName("An") == True
        
    def testsearchStById(self):
        studentsList = StudentList()
        
        s1 = Student(1, "Adrian")
        s2 = Student(5, "Bianca")
        s3 = Student(9, "Cristi")
        
        studentsList.add(s1)
        studentsList.add(s2)
        studentsList.add(s3)
        
        assert studentsList.searchStById(1) == True
        assert studentsList.searchStById(2) == False
        assert studentsList.searchStById(21) == False   
        
        
        
        
        