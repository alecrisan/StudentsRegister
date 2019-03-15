'''
Created on Nov 7, 2017

@author: Ale
'''
from unittest import TestCase

from Assignment0507.domain.Grade import *
from Assignment0507.repository.GradeRepo import *

class TestsGrade(TestCase):
    def testAdd(self):
        gradesList = GradeList()

        gradesList.add((Grade(1, 3, 10)))
        gradesList.add((Grade(5, 2, 9)))
        gradesList.add((Grade(9, 2, 6)))
        
        assert gradesList.gradesList[0].getStId() == 1
        assert gradesList.gradesList[1].getStId() == 5
        assert gradesList.gradesList[2].getStId() == 9
        
        assert len(gradesList.gradesList) == 3
        
    def testRemoveGrForSt(self):
        gradesList = GradeList()
        
        gradesList.add(Grade(1, 3, 10))
        gradesList.add(Grade(5, 2, 9))
        gradesList.add(Grade(9, 2, 6))
        
        gradesList.removeGrForSt(5)
        
        assert len(gradesList.gradesList) == 2
        
    def testRemoveGrForD(self):
        gradesList = GradeList()
        
        gradesList.add(Grade(1, 3, 10))
        gradesList.add(Grade(5, 2, 9))
        gradesList.add(Grade(9, 2, 6))
        
        gradesList.removeGrForD(3)
        
        assert len(gradesList.gradesList) == 2
    
        
    def testfindGrBySt(self):
        gradesList = GradeList()
        
        g1 = Grade(1, 3, 10)
        g2 = Grade(5, 2, 9)
        g3 = Grade(9, 2, 6)
        
        gradesList.add(g1)
        gradesList.add(g2)
        gradesList.add(g3)
        
        assert gradesList.findGrBySt(1) == g1
        assert gradesList.findGrBySt(5) == g2
        assert gradesList.findGrBySt(9) == g3
        assert gradesList.findGrBySt(2) is None

    def testfindGrByD(self):
        gradesList = GradeList()
        
        g1 = Grade(1, 3, 10)
        g2 = Grade(5, 2, 9)
        g3 = Grade(9, 2, 6)
        
        gradesList.add(g1)
        gradesList.add(g2)
        gradesList.add(g3)
        
        assert gradesList.findGrByD(3) == g1
        assert gradesList.findGrByD(2) == g2
        assert gradesList.findGrByD(4) is None
        
    def testgetStId(self):
        g1 = Grade(1, 3, 10)
        g2 = Grade(5, 2, 9)
        g3 = Grade(9, 2, 6)
        
        assert g1.getStId() == 1
        assert g2.getStId() == 5
        assert g3.getStId() == 9
        
    def testgetDiscId(self):
        g1 = Grade(1, 3, 10)
        g2 = Grade(5, 2, 9)
        g3 = Grade(9, 2, 6)
        
        assert g1.getDiscId() == 3
        assert g2.getDiscId() == 2
        assert g3.getDiscId() == 2
        
    def testgetGrValue(self):
        g1 = Grade(1, 3, 10)
        g2 = Grade(5, 2, 9)
        g3 = Grade(9, 2, 6)
        
        assert g1.getGrValue() == 10
        assert g2.getGrValue() == 9
        assert g3.getGrValue() == 6
        
    def testcheckGr(self):
        gradesList = GradeList()
        assert gradesList.checkGr(10) == 10
        assert gradesList.checkGr(35) == None
        assert gradesList.checkGr(0) == None
        
    def testenroll(self):
        gradesList = GradeList()
        
        gradesList.enroll(Grade(1, 2, "none"))
        gradesList.enroll(Grade(2, 3, "none"))
        
        assert len(gradesList.gradesList) == 2
        
    def testcheckIfEnr(self):
        gradesList = GradeList()
        
        gradesList.enroll(Grade(1, 2, "none"))
        gradesList.enroll(Grade(2, 3, "none"))
        
        assert gradesList.checkIfEnr(1, 2) == True
        assert gradesList.checkIfEnr(1, 3) == False
        
    def testgetAvgForSt(self):
        gradesList = GradeList()

        gradesList.add((Grade(1, 3, 10)))
        gradesList.add((Grade(1, 3, 5)))
        gradesList.add((Grade(9, 2, 6)))
        
        assert gradesList.getAvgGrForSt(1, 3) == 7.5
        assert gradesList.getAvgGrForSt(1, 2) == 0
        
    def testgetAvgForDisc(self):
        gradesList = GradeList()

        gradesList.add((Grade(1, 3, 10)))
        gradesList.add((Grade(1, 3, 5)))
        gradesList.add((Grade(9, 2, 6)))
        
        assert gradesList.getAvgForDisc(3) == 7.5
        assert gradesList.getAvgForDisc(2) == 6
        assert gradesList.getAvgForDisc(1) == 0
        
    def testgetAggregatedAvg(self):
        gradesList = GradeList()

        gradesList.add((Grade(1, 3, 10)))
        gradesList.add((Grade(1, 3, 5)))
        gradesList.add((Grade(1, 2, 6)))
        
        assert gradesList.getAggregatedAvg(1) == 7
        assert gradesList.getAggregatedAvg(2) == 0
        
    def testcheckIfFailing(self):
        gradesList = GradeList()

        gradesList.add((Grade(1, 3, 10)))
        gradesList.add((Grade(1, 3, 5)))
        gradesList.add((Grade(1, 2, 4)))
        
        assert gradesList.checkIfFailing(1, 3) == False
        assert gradesList.checkIfFailing(1, 2) == True
        
    def testbestSchoolSituation(self):
        gradesList = GradeList()

        gradesList.add(Grade(1, 3, 10))
        gradesList.add(Grade(1, 3, 6))
        gradesList.add(Grade(9, 2, 6))
        
        auxList = [BestSchoolSit(1, 8.0), BestSchoolSit(9, 6.0)]
        
        assert len(gradesList.bestSchoolSituation()) == 2 
        
    def testallStFailing(self):
        gradesList = GradeList()

        gradesList.add(Grade(1, 3, 3))
        gradesList.add(Grade(2, 3, 4))
        gradesList.add(Grade(9, 2, 6))
        
        auxList = [AllStudents(1, 3, 3.0), AllStudents(2, 3, 4.0)]
        
        assert len(gradesList.allStFailing()) == 2
        
    def testallStEnrolled(self):
        gradesList = GradeList()

        gradesList.add(Grade(1, 3, 10))
        gradesList.add(Grade(1, 3, 8))
        gradesList.add(Grade(9, 3, 6))
        
        auxList = [AllStudents(1, 3, 9.0), AllStudents(9, 3, 6.0)]
        
        assert len(gradesList.allStEnrolled(3)) == 2
        
    def testallDisciplines(self):
        gradesList = GradeList()

        gradesList.add(Grade(1, 3, 10))
        gradesList.add(Grade(1, 3, 8))
        gradesList.add(Grade(9, 2, 6))
        
        auxList = [AllDisciplines(3, 9.0), AllDisciplines(2, 6.0)]
        
        assert len(gradesList.allDisciplines()) == 2
        
    def testfilterGrades(self):
        gradesList = GradeList()
        
        gradesList.add(Grade(1, 3, 10))
        gradesList.add(Grade(1, 3, 8))
        gradesList.add(Grade(9, 2, 6))
        
        assert len(gradesList.filterGrades(None, Discipline(3, "Algebra"))) == 2
        
                
        
        
    