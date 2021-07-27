import random

uniqueidarray = []
for init in range(10):
    string = " "
    uniqueidarray.append(string)


uniqueid = random.randint(100, 999)
uniqueidarray[0] = uniqueid
print(uniqueidarray)
def generateid():
    global uniqueidarray
    for i in range(1, 10):
        uniqueid = random.randint(100, 999)

        while uniqueid == uniqueidarray[i]:
            print("That ID exists")
            uniqueid = random.randint(100, 999)

        if uniqueidarray[i] == " ":
            uniqueidarray[i] = uniqueid





generateid()

print(uniqueidarray)

