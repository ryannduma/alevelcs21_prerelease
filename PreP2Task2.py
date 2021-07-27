# task2.1


for j in range(0, 2):  # for how many students?
    print("Please input your StudentID, email and date of birth")
    studentid = str(input())
    email = str(input())

    dateofbirth = str(input("for the date of birth write in ddmmyyyy and month should be a two digit number"))
    newstring = studentid+email+dateofbirth
    f = open("studentfile.txt", "a")
    f.writelines(newstring)
    f.writelines("\n")
    f.close()


# task2.2


def searchforid(s_id):
    studid = str(s_id)

    filehandle = open("studentfile.txt", "r")
    lineoftext = filehandle.readline()
    found = False
    while lineoftext != '':
        x = lineoftext[0:6] # extract the student ID

        if x == studid:
            found = True
            y = lineoftext[6: len(lineoftext)]
            z = y[0:-9]

            print("This student's email is:", z)
            break
    if found: # how do i make it print this student ID does not exist, if it has reached eof
        print("That student ID does not exist")

        lineoftext = filehandle.readline()

    filehandle.close()


searchforid("rn1234")


# task2.3


def searchforsub(sub_id):  # substring id
    studid = str(sub_id)

    filehandle = open("studentfile.txt", "r")
    lineoftext = filehandle.readline()
    found = False
    while lineoftext != '':
        x = lineoftext[0:2]  # extract the (initials)

        if x == studid:
            found = True
            y = lineoftext[0:6]
            print("This student's StudentID is:", y)

        elif found: # how do i make it print this student ID does not exist, if it has reached eof?
            print("That student ID does not exist")

        lineoftext = filehandle.readline()

    filehandle.close()


searchforsub("rn")



# task2.4

def write(text):
    f = open("studentfile.txt", "w")
    line = f.writelines(text)
    f.close()


write("hI my name is Ryan") 
