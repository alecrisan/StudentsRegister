'''
Created on Nov 5, 2017

@author: Ale
'''
from Assignment0507.controller.StudentFunctions import *
from Assignment0507.controller.DisciplineFunctions import *
from Assignment0507.controller.GradeFunctions import *
from Assignment0507.repository.StudentRepo import *
from Assignment0507.repository.DisciplineRepo import *
from Assignment0507.repository.GradeRepo import *
from Assignment0507.domain.UIException import UIException
from Assignment0507.domain.InitData import *
from Assignment0507.domain.Grade import *
from Assignment0507.domain.Student import *
from Assignment0507.domain.Discipline import *
from Assignment0507.repository.CSVStudentRepo import *
from Assignment0507.repository.CSVDisciplineRepo import *
from Assignment0507.repository.CSVGradeRepo import *
from Assignment0507.repository.BinaryStudentRepo import *
from Assignment0507.repository.BinaryDisciplineRepo import *
from Assignment0507.repository.BinaryGradeRepo import *

def printHelp():
    """
    Prints out the valid options
    input: -
    output: None
    """
    print("Valid options:")
    print("\t1 - add student")
    print("\t2 - remove student")
    print("\t3 - update student")
    print("\t4 - list students")
    print("\t5 - add discipline")
    print("\t6 - remove discipline")
    print("\t7 - update discipline")
    print("\t8 - list disciplines")
    print("\t9 - help")
    print("\t10 - grade student at a given discipline")
    print("\t11 - list grades")
    print("\t12 - enroll a student at a given discipline")
    print("\t13 - search student by ID/name")
    print("\t14 - search discipline by ID/name")
    print("\t15 - Statistic1: All students enrolled at a given discipline")
    print("\t16 - Statistic2: All students that are failing at one or more disciplines")
    print("\t17 - Statistic3: Students with the best school situation")
    print("\t18 - Statistic4: Disciplines with at least one grade")
    print("\t19 - Undo")
    print("\t20 - Redo")
    print("\t0 - exit")
    
class UI:
    def __init__(self, studentFunctions, disciplineFunctions, gradeFunctions, undoController):
        self.studentFunctions = studentFunctions
        self.disciplineFunctions = disciplineFunctions
        self.gradeFunctions = gradeFunctions
        self.undoController = undoController
    
    def start(self):
        while True:
            option = raw_input("Enter an option: ")
            
            if option == "1":
                print("You chose to add a student")
                try:
                    Id = int(raw_input("Enter an ID: "))
                except ValueError as e:
                    raise UIException("ID must be an integer")
                name = raw_input("Enter a name: ")
                try:
                    studentFunctions.addStudent(Student(Id, name))
                except RepoException as e:
                    print(e)
                    
            elif option == "2":
                print("You chose to remove a s tudent")
                try:
                    Id = int(raw_input("With the ID: "))
                except ValueError as e:
                    raise UIException("ID must be an integer")
                if studentFunctions.findStudent(Id) is None:
                    print("The student doesn't exist")
                else:
                    studentFunctions.removeStudent(Id)
                    while gradeFunctions.findGradeByStudent(Id) is not None:
                    #we also remove all of his grades
                        gradeFunctions.removeGradesForStudent(Id)
                        
            elif option == "3":
                print("Update the student with the following id: ")
                try:
                    Id = int(raw_input("Id: "))
                except ValueError as e:
                    raise UIException("ID must be an integer")
                if studentFunctions.findStudent(Id) is None:
                    #the student we want to update doesn't exist
                    print("That student doesn't exist")
                else:
                    print("Give the new values: ")
                    try:
                        newId = int(raw_input("New ID: "))
                    except ValueError as e:
                        raise UIException("ID must be an integer")
                    newName = raw_input("New name: ")
                    if studentFunctions.findStudent(newId) is None:
                    #the new id isn't already taken
                        studentFunctions.updateStudent(Id, Student(newId, newName))
                    #we delete the old student's grades
                        while gradeFunctions.findGradeByStudent(Id) is not None:
                            gradeFunctions.removeGradesForStudent(Id)
                    else:   
                        print("The new ID is already taken")
                        
            elif option == "4":
                studentFunctions.printList()
            
            elif option == "5":
                print("You chose to add a discipline")
                try:
                    Id = int(raw_input("Enter an ID: "))
                except ValueError as e:
                    raise UIException("ID must be an integer")
                name = raw_input("Enter a name: ")
                try:
                    disciplineFunctions.addDiscipline(Discipline(Id, name))
                except RepoException as e:
                    print(e)
               
            elif option == "6":
                print("You chose to remove a discipline")
                try:
                    Id = int(raw_input("With the ID: "))
                except ValueError as e:
                    raise UIException("ID must be an integer")
                if disciplineFunctions.findDiscipline(Id) is None:
                    print("The discipline doesn't exist")
                else:
                    disciplineFunctions.removeDiscipline(Id)
                    while gradeFunctions.findGradeByDiscipline(Id) is not None:
                    #we also remove all of the grades at that discipline
                        gradeFunctions.removeGradesForDiscipline(Id)
                        
            elif option == "7":
                print("Update the discipline with the following id: ")
                try:
                    Id = int(raw_input("Id: "))
                except ValueError as e:
                    raise UIException("ID must be an integer")
                if disciplineFunctions.findDiscipline(Id) is None:
                    #the discipline we want to update doesn't exist
                    print("That discipline doesn't exist")
                else:
                    print("Give the new values: ")
                    try:
                        newId = int(raw_input("New ID: "))
                    except ValueError as e:
                        raise UIException("ID must be an integer")
                    newName = raw_input("New name: ")
                    if disciplineFunctions.findDiscipline(newId) is None:
                    #the new id isn't already taken
                        disciplineFunctions.updateDiscipline(Id, Discipline(newId, newName))
                    #we delete the old discipline's grades
                        while gradeFunctions.findGradeByDiscipline(Id) is not None:
                            gradeFunctions.removeGradesForDiscipline(Id)
                    else:   
                        print("The new ID is already taken")
            
            elif option == "8":
                disciplineFunctions.printList()
                
            elif option == "9":
                printHelp()
            
            elif option == "10":
                print("You chose to grade a student at a given discipline")
                try:
                    studentId = int(raw_input("Enter the student's ID: "))
                except ValueError as e:
                    raise UIException("ID must be an integer")
                try:
                    disciplineId = int(raw_input("Enter the discipline ID you want to grade at: "))
                except ValueError as e:
                    raise UIException("ID must be an integer")
                if studentFunctions.findStudent(studentId) is None:
                    print("The student doesn't exist")
                elif disciplineFunctions.findDiscipline(disciplineId) is None:
                    print("The discipline doesn't exist")
                else:
                    if gradeFunctions.checkIfEnrolled(studentId, disciplineId) is None:
                        print("Student is not enrolled at the given discipline")
                    else:
                        try:
                            grade_value = int(raw_input("Enter the grade: "))
                        except ValueError as e:
                            raise UIException("Grade must be an integer")
                        if gradeFunctions.checkGrade(grade_value) is None:
                            print("Grade is not between 1 and 10")
                        else:
                            gradeFunctions.addGrade(Grade(studentId, disciplineId, grade_value))
                            
            elif option == "11":
                if gradeFunctions.lenn(gradeFunctions) > 0:
                    gradeFunctions.printList(disciplineFunctions, studentFunctions)
                else:
                    print("Sorry. The list is empty.")
            
            elif option == "12":
                print("You chose to enroll a student at a discipline")
                try:
                    studentId = int(raw_input("Enter the student's ID: "))
                except ValueError as e:
                    raise UIException("ID must be an integer")
                try:
                    disciplineId = int(raw_input("Enter the discipline ID you want to enroll at: "))
                except ValueError as e:
                    raise UIException("ID must be an integer")
                if studentFunctions.findStudent(studentId) is None:
                    print("The student doesn't exist")
                elif disciplineFunctions.findDiscipline(disciplineId) is None:
                    print("The discipline doesn't exist")
                else:
                    gradeFunctions.enrollStudent(Grade(studentId, disciplineId, grade_value="none"))
                    
            elif option == "13":
                print("You chose to search a student")
                opt = raw_input("ID/name?")
                if opt == 'name':
                    name = raw_input("Enter the name: ")
                    if studentFunctions.searchStudentByName(name) == False:
                        print("No matches")
                elif opt == 'ID':
                    try:
                        Id = int(raw_input("Enter the ID: "))
                    except ValueError as e:
                        raise UIException("ID must be an integer")
                    if studentFunctions.searchStudentById(Id) == False:
                        print("No matches")
                else:
                    print("Invalid choice")
                        
            elif option == "14":
                print("You chose to search a discipline")
                opt = raw_input("ID/name?")
                if opt == 'name':
                    name = raw_input("Enter the name: ")
                    if disciplineFunctions.searchDisciplineByName(name) == False:
                        print("No matches")
                elif opt == 'ID':
                    try:
                        Id = int(raw_input("Enter the ID: "))
                    except ValueError as e:
                        raise UIException("ID must be an integer")
                    if disciplineFunctions.searchDisciplineById(Id) == False:
                        print("No matches")
                else:
                    print("Invalid choice")
                        
            elif option == '15':
                print("Statistic1: All students enrolled at a given discipline")
                try:
                    Id = int(raw_input("Enter a discipline's ID: "))
                except ValueError as e:
                    raise UIException("ID must be an integer")
                sortedlist = gradeFunctions.statistics1(Id)
                if len(sortedlist) == 0:
                    print("No students enrolled at that discipline")
                else:
                    for item in sortedlist:
                        print("Student: " + studentFunctions.getStudentName(item.getStId()) + " Discipline: " + disciplineFunctions.getDisciplineName(item.getDiscId()) + " Aggregated average: " + str(item.getAvg()))
                
            elif option == '16':
                print("Statistic2: All students that are failing at one or more disciplines")
                sortedlist = gradeFunctions.statistics2()
                if len(sortedlist) == 0:
                    print("No students failing")
                else:
                    for item in sortedlist:
                        print("Student: " + studentFunctions.getStudentName(item.getStId()) + " Discipline: " + disciplineFunctions.getDisciplineName(item.getDiscId()) + " Aggregated average: " + str(item.getAvg()))
                
            elif option == '17':
                print("Statistic3: Students with the best school situation")
                sortedlist = gradeFunctions.statistics3()
                if len(sortedlist) == 0:
                    print("No students graded")
                else:
                    for item in sortedlist:
                        print("Student: " + studentFunctions.getStudentName(item.getStId()) + " Aggregated average: " + str(item.getAvg()))
                
            elif option == '18':
                print("Statistic4: Disciplines with at least one grade, in descending order of the average")
                sortedlist = gradeFunctions.statistics4()
                if len(sortedlist) == 0:
                    print("No grades at any discipline")
                else:
                    for item in sortedlist:
                        print("Discipline: " + disciplineFunctions.getDisciplineName(item.getDiscId()) + " Average grade: " + str(item.getAvg()))
                
            elif option == '19':
                if undoController.undo() == False:
                    print("Could not perform undo")
                    
            elif option == '20':
                if undoController.redo() == False:
                    print("Could not perform redo")
                    
            elif option == "0":
                print("Exited the program")
                break
            
            else:
                print("Not a valid option. Enter 9 if you need help :)")
    
def readSettingsFile():
        settings = list()

        file = open("settings.properties", "r")

        for line in file:
            attributes = line.split("=")

            if len(attributes) > 1:
                settingsItem = attributes[1].strip()
            else:
                settingsItem = ""

            settings.append(settingsItem)

        file.close()
        return settings

def loadData(settings):
        if settings[0] == "inmemory":
            return StudentList(), DisciplineList(), GradeList()
        elif settings[0] == "binaryfiles":
            return BinaryStudentList(settings[1]), BinaryDisciplineList(settings[2]), BinaryGradeList(settings[3])
        elif settings[0] == "csvfiles":
            return CSVStudentList(settings[1]), CSVDisciplineList(settings[2]), CSVGradeList(settings[3])
                   
settings = readSettingsFile()
studentsList, disciplinesList, gradesList = loadData(settings)

if settings[0] == "inmemory":
    initStudentsList(studentsList)
    initDisciplinesList(disciplinesList)
    initGradesList(gradesList)

undoController = UndoController()
gradeFunctions = GradeFunct(gradesList, undoController)
studentFunctions = StudentFunct(studentsList, undoController, gradeFunctions)
disciplineFunctions = DisciplineFunct(disciplinesList, undoController, gradeFunctions)



menu = UI(studentFunctions, disciplineFunctions, gradeFunctions, undoController)
menu.start()
