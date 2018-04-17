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

class Node:
    y = puzzle()