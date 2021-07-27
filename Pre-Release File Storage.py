import random
books = []
for init in range(10):
    string = " "
    books.append(string)
print(books)


def updatebookrecord():
    global books
    uniqueidarray = []
    for init in range(2):
        string = " "
        uniqueidarray.append(string)

    uniqueid = random.randint(100, 999)
    uniqueidarray[0] = uniqueid
    print(uniqueidarray)

    for i in range(1, 2):
        uniqueid = random.randint(100, 999)

        while uniqueid == uniqueidarray[i]:
            uniqueid = random.randint(100, 999)

        if uniqueidarray[i] == " ":
            uniqueidarray[i] = uniqueid


    print(uniqueidarray)

    for i in range(len(uniqueidarray)):

        booktitle = str(input("Enter the book title = "))
        mainauthor = str(input("Please input the main author of thr book = "))
        yearofpub = str(input("Enter the year of publication = "))
        bookid = str(uniqueidarray[i])
        recordstring = bookid + "*" + booktitle + "*" + mainauthor + "*" + yearofpub

        if books[i] == " ":
           books[i] = recordstring
           print(books)
        elif i >= 10:
           print("Storage full")


def printbookrecord():

    for j in range(len(books)):
        print(books[j])



def putrecordinfile():
    global books
    filehandle = open("bookrecord.txt", "a")
    for index in range(len(books)):
        if books[index] != " ":
            newstring = str(books[index])
            print(newstring)
            filehandle.write(newstring)
            filehandle.write("\n")

    filehandle.close()


def readserialfile():
    filehandle = open("bookrecord.txt", "r")
    lineoftext = filehandle.readline()
    while lineoftext != '':
        lineoftext = lineoftext.rstrip("\n")
        print(lineoftext)
        lineoftext = filehandle.readline()
    filehandle.close()


#updatebookrecord()
#printbookrecord()


#putrecordinfile()
#readserialfile()
