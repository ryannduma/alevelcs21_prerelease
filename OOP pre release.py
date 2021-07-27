class tools:
    def __init__(self, name,cost,filename):
        self.name = name
        self.cost = cost
        self.filename = filename

    def setname(self, toolname):
        self.name = toolname
        return self.name

    def setcost(self,costoftool):
        self.cost = costoftool
        return self.cost

    def setfile(self, nameoffile):
        self.filename = nameoffile
        return self.filename

    def gettoolname(self):
        return self.name

    def gettoolcost(self):
        return self.cost

    def gettoolfile(self):
        return self.filename


class shelf(tools):
    shelves = []
    def __init__(self, name, cost, filename):
        tools.__init__(self, name, cost, filename)
        for i in range(0, 4):
            self.shelves.append([])
            for j in range(10):
                self.shelves[i].append(tools(" ", " ", " "))

    def addnewtool(self, toolname,costoftool, nameoffile,shelfnum, shelfpos):

        self.name = toolname
        self.cost = costoftool
        self.filename = nameoffile
        newtool = "toolname = " + str(self.name) + " | " + "toolcost = " + str(self.cost) + " | " + "toolfilename = " + str(self.filename)

        self.shelves[shelfpos][shelfnum] = newtool

    def showtools(self, pos):

        for i in range(10):
            print(self.shelves[pos][i])


tool = tools("wedge", 20, "abc.txt")
newtol = shelf("wrench", 20, "abc.txt")
newtol.addnewtool("wer", 22, "wer.txt", 6, 3)
newtol.showtools(3)










