# arrays
# task1.1
"""
StudentData = []


def initialisearray():
    for i in range(0, 1):
        blank = ""
        StudentData.append(blank)


def populatearray():
    for j in range(len(StudentData)):
        print("Please input your name, email and date of birth")
        name = str(input())
        email = str(input())
        dateofbirth = str(input("for the date of birth write in dd/mm/yyyy and month should be a two digit number"))
        newstring = name + "*" + email + "*" + dateofbirth
        StudentData[j] = newstring


def readfromarray():
    print("Student Name", "       ", "Email", "   ", "Date of Birth")  # column header identifier

    for n in range(len(StudentData)):
        if StudentData[n] != "":  # part of task 1.2
            print(StudentData[n])



initialisearray()
populatearray()
readfromarray()


# task1.2

def deleteastudentac(d): # d is the parameter that takes the student's name to delete
    name = str(d)
    for j in range (len(StudentData)):
        x = StudentData[j]
        splitstring = x.split('*', 1)
        if name == splitstring[0]:
            deleted = StudentData.pop(j)
            StudentData[j] = ""
            return deleted


# task1.3

def searcharray(n):
    name = str(n)
    for j in range (len(StudentData)):
        x = StudentData[j]
        splitstring = x.split('*', 1)
        if name == splitstring[0]:
            emailsplit = x.split('*', 3)
            print("The email address for:", name, "is:", emailsplit[1])
            return emailsplit
# task1.4


def outputbirthmonth(m, emailsplit):
    month = str(m)  # user input month
    birthday = emailsplit[2]  # take the split value of the birthdate from search array function
    y = birthday.split('/', 3)  # split the birthday into dd/mm/yyyy
    birthmonth = y[1]  # isolate the mm (month)
    for k in range(len(StudentData)):
        if month == birthmonth:  # if the months match
            x = StudentData[k]
            splitstring = x.split('*', 3)
            studentname = splitstring[0]  # take the name
            dateofbirth = splitstring[2]  # take the full birth date
            print("Student:", studentname, " Date of Birth", dateofbirth)  # print their name and date of birth
"""
# task1.5 make the above work for a 2d array


rows, cols = (2, 5)
StudentData2d = [[" "] * cols] * rows


def populatearray():
    for r in range(len(StudentData2d)):

        print("Please input your name, email and date of birth,StudentID, TutorID")
        name = str(input())
        StudentData2d[r][0] = name
        email = str(input())
        StudentData2d[r][1] = email
        dateofbirth = str(input("for the date of birth write in dd/mm/yyyy and month should be a two digit number"))
        StudentData2d[r][2] = dateofbirth
        studentid = str(input())
        StudentData2d[r][3] = studentid
        tutorid = str(input())
        StudentData2d[r][4] = tutorid


populatearray()


def readfromarray():
    print("Student Name", "       ", "Email", "   ", "Date of Birth", "      ", "StudentID", "   ", "TutorID")

    for n in range(len(StudentData2d)):
        if StudentData2d[n] != "":  # part of task 1.2 do not read if blank
            print(StudentData2d[n])


readfromarray()


# task1.2

def deleteastudentac(d): # d is the parameter that takes the student's name to delete
    name = str(d)
    for j in range(len(StudentData2d)):
        x = StudentData2d[j][0]
        if name == x:
            deleted = StudentData2d.pop(j)
            StudentData2d[j] = ""
            return deleted


# task1.3

def searcharray(n):
    name = str(n)
    for j in range(len(StudentData2d)):
        x = StudentData2d[j][0]
        if name == x:
            print("The email address for:", name, "is:", StudentData2d[j][1])
            return StudentData2d[j][1]
# task1.4


def outputbirthmonth(m):
    month = str(m)  # user input month

    for k in range(len(StudentData2d)):
        birthday = StudentData2d[k][3]  # take the split value of the birthdate from search array function
        y = birthday.split('/', 3)  # split the birthday into dd/mm/yyyy
        birthmonth = y[1]  # isolate the mm (month)
        if month == birthmonth:  # if the months match
            studentname = StudentData2d[k][0]  # take the name
            dateofbirth = StudentData2d[k][3]  # take the full birth date
            print("Student:", studentname, " Date of Birth", dateofbirth)  # print their name and date of birth
