class puzzle:
    chickensLeft = 0
    chickensRight = 0
    wolvesLeft = 0
    wolvesRight = 0
    boatBank = 0

    def moveAnimals(self, numChickens, numWolves):
        if self.boatBank is 0: #boat is on left bank
            self.chickensLeft = self.chickensLeft - numChickens
            self.chickensRight = self.chickensRight + numChickens
            self.wolvesLeft = self.wolvesLeft - numWolves
            self.wolvesRight = self.wolvesRight + numWolves
            boatBank = 1
        elif boatBank is 1: #boat is on right bank
            self.chickensLeft = self.chickensLeft + numChickens
            self.chickensRight = self.chickensRight - numChickens
            self.wolvesLeft = self.wolvesLeft + numWolves
            self.wolvesRight = self.wolvesRight - numWolves
            self.boatBank = 0

    def printBoat(self):
        if self.boatBank is 0:
            print("Boat is at Left Bank")    
        else:
            print("Boat is at Right Bank")

    def isMoveValid(self, numChickens, numWolves):
        if numChickens + numWolves < 1:
            return False
        currChick = 0
        currWolves = 0
        otherChick = 0
        otherWolves = 0
        if self.boatBank is 0:
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
                if (currChick - numChickens) >= (currWolves - numWolves):
                    if (otherChick + numChickens) >= (otherWolves + numWolves):
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

class Node:
    y = puzzle()