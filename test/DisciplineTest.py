'''
Created on Nov 7, 2017

@author: Ale
'''
from unittest import TestCase
from Assignment0507.domain.Discipline import *
from Assignment0507.repository.DisciplineRepo import *


class TestsDiscipline(TestCase):
    def testAdd(self):
        disciplinesList = DisciplineList()
        
        disciplinesList.add((Discipline(1, "Algebra")))
        disciplinesList.add((Discipline(4, "English")))
        disciplinesList.add((Discipline(8, "Chemistry")))
        
        assert disciplinesList.disciplinesList[0].getId() == 1
        assert disciplinesList.disciplinesList[1].getId() == 4
        assert disciplinesList.disciplinesList[2].getId() == 8
        
    def testRemove(self):
        disciplinesList = DisciplineList()
        
        disciplinesList.add(Discipline(1, "Algebra"))
        disciplinesList.add(Discipline(4, "English"))
        disciplinesList.add(Discipline(8, "Chemistry"))
    
        disciplinesList.removeDisc(Discipline(4, "English"))
        
        assert disciplinesList.disciplinesList[1].getId() == 4
   
    def testUpdate(self):
        disciplinesList = DisciplineList()
        
        disciplinesList.add(Discipline(1, "Algebra"))
        disciplinesList.add(Discipline(4, "English"))
        d3 = Discipline(8, "Chemistry")
        
        
        disciplinesList.update(4, d3)
        
        assert disciplinesList.disciplinesList[1].getId() == 8
        assert disciplinesList.disciplinesList[1].getName() == "Chemistry"
        
    def testfindDById(self):
        disciplinesList = DisciplineList()
        
        d1 = Discipline(1, "Algebra")
        d2 = Discipline(4, "English")
        d3 = Discipline(8, "Chemistry")
        
        disciplinesList.add(d1)
        disciplinesList.add(d2)
        disciplinesList.add(d3)
        
        assert disciplinesList.findDById(1) == d1
        assert disciplinesList.findDById(4) == d2
        assert disciplinesList.findDById(8) == d3
        assert disciplinesList.findDById(2) is None
        
    def testgetDName(self):
        disciplinesList = DisciplineList()
        
        d1 = Discipline(1, "Algebra")
        d2 = Discipline(4, "English")
        d3 = Discipline(8, "Chemistry")
        
        disciplinesList.add(d1)
        disciplinesList.add(d2)
        disciplinesList.add(d3)
        
        assert disciplinesList.getDName(1) == "Algebra"
        assert disciplinesList.getDName(4) == "English"
        assert disciplinesList.getDName(8) == "Chemistry"
        assert disciplinesList.getDName(2) is None
        
    def testgetId(self):
        d1 = Discipline(1, "Algebra")
        d2 = Discipline(4, "English")
        d3 = Discipline(8, "Chemistry")
        
        assert d1.getId() == 1
        assert d2.getId() == 4
        assert d3.getId() == 8
        
    def testgetName(self):
        d1 = Discipline(1, "Algebra")
        d2 = Discipline(4, "English")
        d3 = Discipline(8, "Chemistry")
        
        assert d1.getName() == "Algebra"
        assert d2.getName() == "English"
        assert d3.getName() == "Chemistry"
        
    def testsearchDByName(self):
        disciplinesList = DisciplineList()
        
        d1 = Discipline(1, "Algebra")
        d2 = Discipline(4, "English")
        d3 = Discipline(8, "Chemistry")
        
        disciplinesList.add(d1)
        disciplinesList.add(d2)
        disciplinesList.add(d3)
        
        assert disciplinesList.searchDByName("English") == True
        assert disciplinesList.searchDByName("Abc") == False
        assert disciplinesList.searchDByName("E") == True
        
    def testsearchDById(self):
        disciplinesList = DisciplineList()
        
        d1 = Discipline(1, "Algebra")
        d2 = Discipline(4, "English")
        d3 = Discipline(8, "Chemistry")
        
        disciplinesList.add(d1)
        disciplinesList.add(d2)
        disciplinesList.add(d3)
        
        assert disciplinesList.searchDById(4) == True
        assert disciplinesList.searchDById(45) == False
        assert disciplinesList.searchDById(8) == True
        
        
        
        