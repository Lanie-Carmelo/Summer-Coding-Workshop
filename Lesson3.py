studentName = []
assignments = ["Assignment1", "Assignment2", "Assignment3", "Assignment4", "Assignment5"]
grade = []

def addStudent():
  newStudent = input("Enter students name: ")
  studentName.append(newStudent)

def computeGrade():
  sum = 0
  for i in assignments:
    assignmentGrade = input("Enter the grade for " + i +": ")
    sum += int(assignmentGrade)
  finalGrade = sum / len(assignments)
  grade.append(finalGrade)

def printGrades():
  i = 0
  j = 0
  while i < len(studentName):
    while j < len(grade):
      print(studentName[i] + " " +str(grade[j]))
      j += 1
      i += 1

classSize = 2
numOfStudents = 0
while numOfStudents < classSize:
  addStudent()
  computeGrade()
  numOfStudents+=1

printGrades()
