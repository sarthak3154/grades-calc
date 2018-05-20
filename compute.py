import sys
import operator

grades = {0:"C", 1: "B-", 2: "B", 3: "B+", 4: "A-", 5: "A", 6: "A+", 7: "A+"}
percentage = {"a1": 7.5, "a2": 7.5, "pr": 25, "t1": 30, "t2": 30}
maximum = {}
students = {}
class Student:
    def __init__(self, id, first_name, last_name):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name

    def addComponentBasedMarks(self, component, value):
        vars(self)[component] = int(value.rstrip())

    def calculateTotal(self):
        total = 0
        for key in percentage:
            if hasattr(self, key):
                total += round(float(vars(self)[key]/int(maximum.get(key))) * percentage.get(key), 2)
        self.total = round(total, 2)

    def calculateGrade(self, qualify_point):
        grade_range = int((100 - qualify_point)/7)
        if self.total < qualify_point:
            self.grade = "F"
        else:
            grade = int((self.total - qualify_point) / grade_range)
            self.grade = grades.get(grade)

def calculateStudentGrades(qualify_point=50):
    for key in students:
        students[key].calculateTotal()
        students[key].calculateGrade(qualify_point)

def displayIndividualComponent():
    component = input("Enter Component Name: ")
    component_name = component.rstrip().lower()
    print("\n" + component.rstrip().upper() + " grades (" + maximum.get(component_name) + ")")
    for key, value in students.items():
        if hasattr(value, component_name):
            print(key + "\t" + value.last_name + ", " + value.first_name + "\t" + str(vars(value)[component_name]))

def displayAverageComponent():
    component = input("Enter Component Name: ")
    component_name = component.rstrip().lower()
    sum = 0
    for key, value in students.items():
        if hasattr(value, component_name):
            sum += float(vars(value)[component_name])
    average = round(sum/len(students), 2)
    print(component_name.upper() + " average: " + str(average) + "/" + maximum.get(component_name))

def displayReport(list):
    print()
    print('{0:5} {1:6} {2:6}'.format("ID", "LN", "FN"), end="")
    print("A1\tA2\tPR\tT1\tT2\tGR\tFL")
    for value in list:
        print('{0:5} {1:6} {2:6}'.format(value.id, value.last_name,
            value.first_name), end="")
        for key in maximum:
            if hasattr(value, key):
                print(str(vars(value)[key]) + "\t", end="")
            else:
                 print("\t", end="")
        print(str(value.total) + "\t" + value.grade)

def displayStandardReport():
    list = sorted(students.values(), key=operator.attrgetter('id'))
    displayReport(list)

def displaySortedResults():
    sort_order = input("Enter the sorting order: LT (last name) and GR (numeric grade)\n")
    sort_order = sort_order.lower()
    sorted_students = []
    if sort_order == "lt":
        sorted_students = sorted(students.values(), key=operator.attrgetter('last_name'))
        displayReport(sorted_students)
    elif sort_order == "gr":
        sorted_students = sorted(students.values(), key=operator.attrgetter('total'))
        displayReport(sorted_students)
    else:
        print("Invalid Input.")

def changeClearingPoint():
    clear_point = input("Enter the Pass/Fail marks: ")
    if clear_point.isalpha():
        print("Invalid Input.")
    else:
        calculateStudentGrades(int(clear_point))
        displayStandardReport()

def exit():
    print("Good Bye")
    sys.exit()
