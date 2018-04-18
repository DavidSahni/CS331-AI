from classFile import puzzle
import sys


def readFile(initFile, game):
    filePtr = open(initFile, 'r')
    data = filePtr.readline()
    leftSide = data.split(',')
    game.chickensLeft = int(leftSide[0])
    game.wolvesLeft = int(leftSide[1])
    game.boatBank = int(leftSide[2])

    data = filePtr.readline()
    filePtr.close()
    rightSide = data.split(',')
    game.chickensRight = int(rightSide[0])
    game.wolvesRight = int(rightSide[1])

def printGame(game):
    print("Left Side Counts:")
    print("Chickens: ", game.chickensLeft)
    print("Wolves: ", game.wolvesLeft)
    print("Right Side Counts:")
    print("Chickens: ", game.chickensRight)
    print("Wolves: ", game.wolvesRight)
    game.printBoat()

def isPuzzleEqual(x, goal):
    retval = True
    if (x.chickensLeft != goal.chickensLeft):
        retval = False
    if (x.chickensRight != goal.chickensRight):
        retval = False
    if (x.wolvesLeft != goal.wolvesLeft):
        retval = False
    if (x.wolvesRight != goal.wolvesRight):
        retval = False
    if (x.boatBank != goal.boatBank):
        retval = False
    return retval

def bfs(start, goal):
    closed = {}
    fringe = [start]
    while True:
        node = fringe.pop()
        if len(fringe) < 1:
            return None
        if isPuzzleEqual(node.state, goal) is True:
            return node
        else:
            if inClosed(closed, node.state) is False:
                addClosed(closed, node.state)
                #fringe.append(Expand(node))
            

def inClosed(closed, target):
    inSet = False
    for i in closed.keys():
        if isPuzzleEqual(target, closed[i]) is True:
            inSet = True
            break
    return inSet

def addClosed(closed, state):
    i = len(closed)
    closed[i] = state


initFile = ""
goalFile = ""
outputFile = ""
mode = ""
start = puzzle()

if len(sys.argv) != 5:
    print("Usage: < initial state file > < goal state file > < mode > < output file >")
else:
    initFile = sys.argv[1]
    goalFile = sys.argv[2]
    outputFile = sys.argv[3]
    mode = sys.argv[4] 

readFile(initFile, start)
printGame(start)
x = start.copyToNew()
closed = {}
addClosed(closed, start)
print(inClosed(closed, x))
x.moveAnimals(1, 3)
printGame(x)
print(inClosed(closed, x))
addClosed(closed, x)


