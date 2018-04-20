class puzzle:
    chickensLeft = 0
    chickensRight = 0
    wolvesLeft = 0
    wolvesRight = 0
    boatBank = 0
    numMoved = 0

    def printState(self):
        print(self.chickensLeft, self.wolvesLeft, self.boatBank, sep=", ")
        val = 0
        if (self.boatBank == 0):
            val = 1
        else:
            val = 0
        print(self.chickensRight, self.wolvesRight, val, sep=", ")
        print()
        

    def moveAnimals(self, numChickens, numWolves):
        if self.boatBank == 1: #boat is on left bank
            self.chickensLeft = self.chickensLeft - numChickens
            self.chickensRight = self.chickensRight + numChickens
            self.wolvesLeft = self.wolvesLeft - numWolves
            self.wolvesRight = self.wolvesRight + numWolves
            self.boatBank = 0
        elif self.boatBank == 0: #boat is on right bank
            self.chickensLeft = self.chickensLeft + numChickens
            self.chickensRight = self.chickensRight - numChickens
            self.wolvesLeft = self.wolvesLeft + numWolves
            self.wolvesRight = self.wolvesRight - numWolves
            self.boatBank = 1
        self.numMoved = numChickens + numWolves

    def getAnimalsLeft(self):
        return self.chickensLeft + self.wolvesLeft
    
    def getAnimalsRight(self):
        return self.chickensRight + self.wolvesRight

    def printBoat(self):
        if self.boatBank == 1:
            print("Boat is at Left Bank")
        elif self.boatBank == 0:
            print("Boat is at Right Bank")

    def isMoveValid(self, numChickens, numWolves):
        if numChickens + numWolves < 1:
            return False
        currChick = 0
        currWolves = 0
        otherChick = 0
        otherWolves = 0
        if self.boatBank == 1:
            currChick = self.chickensLeft
            currWolves = self.wolvesLeft
            otherChick = self.chickensRight
            otherWolves = self.wolvesRight
        else:
            otherChick = self.chickensLeft
            otherWolves = self.wolvesLeft
            currChick = self.chickensRight
            currWolves = self.wolvesRight

        valid = False
        if currChick >= numChickens:
            if currWolves >= numWolves:
                newCurrChicks = currChick - numChickens
                if newCurrChicks == 0 or newCurrChicks >= (currWolves - numWolves):
                    newOtherChicks = otherChick + numChickens
                    if newOtherChicks == 0 or newOtherChicks >= (otherWolves + numWolves):
                        valid = True
        return valid

    def copyToNew(self):
        x = puzzle()
        x.chickensLeft = self.chickensLeft
        x.chickensRight = self.chickensRight
        x.wolvesLeft = self.wolvesLeft
        x.wolvesRight = self.wolvesRight
        x.boatBank = self.boatBank
        return x

    def getBankName(self):
        if self.boatBank == 1:
            return 'left'
        elif self.boatBank == 0:
            return 'right'
        return None

class Node:
    State = puzzle()
    parent = None
    pathCost = 0 #number of moves to this point
    orderCount = 0 #maintain order and break heap ties

    def __init__(self, parent, State):
        self.parent = parent
        self.State = State
