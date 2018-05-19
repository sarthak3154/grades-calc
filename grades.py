from compute import *
import os

def readClassFile(file):
    studentsFile = open(file, "r")
    for line in studentsFile:
        data = line.split("|")
        students[data[0]] = Student(data[0], data[1].rstrip(), data[2].rstrip())
    studentsFile.close()

def readGradeFile(file):
    grades = open(file, "r")
    line = grades.readline()
    file_name = file.split(".")[0].rstrip()
    # Store the maximum marks
    maximum[file_name[:2]] = line.rstrip()
    line = grades.readline()
    while line:
        data = line.split("|")
        students[data[0]].addComponentBasedMarks(file_name[:2], data[1])
        line = grades.readline()
    grades.close()

def readGradeFiles(files):
    for file in files:
        readGradeFile(file)

readClassFile("class.txt")
files = ["a1.txt", "a2.txt", "project.txt", "t1.txt", "t2.txt"]
readGradeFiles(files)
calculateStudentGrades()

def displayMenu():
    print("\n1> Display individual component" +
    "\n2> Display component average" +
    "\n3> Display Standard Report" +
    "\n4> Sort by alternate column" +
    "\n5> Change Pass/Fail point" +
    "\n6> Exit" )
    options = {1: displayIndividualComponent, 2: displayAverageComponent,
            3: displayStandardReport, 4: displaySortedResults,
            5: changeClearingPoint, 6: exit}
    option = input("Enter your choice: ")
    if option.isalpha():
        print("Invalid Input. Re-enter the choice")
    else:
        functionToCall = options[int(option)]
        functionToCall()
    input("\n::: Press Enter to Continue :::")
    os.system('clear')
    calculateStudentGrades()
    displayMenu()

displayMenu()
