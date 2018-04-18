from classFile import *
from collections import deque
import sys

#reads in a file to a game (puzzle) object
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

#prints a puzzle
def printGame(game):
    print("Left Side Counts:")
    print("Chickens: ", game.chickensLeft)
    print("Wolves: ", game.wolvesLeft)
    print("Right Side Counts:")
    print("Chickens: ", game.chickensRight)
    print("Wolves: ", game.wolvesRight)
    game.printBoat()

#compares two puzzle states for equality
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

#breadth first search, takes in start state and end state
def bfs(start, goal):
    closed = {}
    startNode = Node(None, start)
    fringe = deque([startNode])
    counter = 0
    while True:
        if len(fringe) < 1:
            return None
        node = fringe.popleft()
        if isPuzzleEqual(node.State, goal) is True:
            print('expanded:', counter, "nodes")
            return node
        else:
            counter += 1 
            if inClosed(closed, node.State) is False:
                addClosed(closed, node.State)
                fringe.extend(expandBfs(node))

#expansion for breadth first search
#just keeps it as a fifo stack
def expandBfs(node):
    succesors = []
    generateSuccesors(succesors, node)
    return succesors

def generateSuccesors(succesors, node):
    state = node.State
    if state.isMoveValid(1, 0):
        x = state.copyToNew()
        x.moveAnimals(1, 0)
        newNode = Node(node, x)
        newNode.moveMessage = "Sent 1 Chicken to " + x.getBankName()
        succesors.append(newNode)
    if state.isMoveValid(2, 0):
        x = state.copyToNew()
        x.moveAnimals(2, 0)
        newNode = Node(node, x)
        newNode.moveMessage = "Sent 2 Chickens to " + x.getBankName()
        succesors.append(newNode)
    if state.isMoveValid(0, 1):
        x = state.copyToNew()
        x.moveAnimals(0, 1)
        newNode = Node(node, x)
        newNode.moveMessage = "Sent 1 Wolf to " + x.getBankName()
        succesors.append(newNode)
    if state.isMoveValid(0, 2):
        x = state.copyToNew()
        x.moveAnimals(0, 2)
        newNode = Node(node, x)
        newNode.moveMessage = "Sent 2 Wolves to " + x.getBankName()
        succesors.append(newNode)
    if state.isMoveValid(1, 1):
        x = state.copyToNew()
        x.moveAnimals(1, 1)
        newNode = Node(node, x)
        newNode.moveMessage = "Sent 1 Chicken and 1 Wolf to " + x.getBankName()        
        succesors.append(newNode)

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

def printSolutionStates(soln):
    if soln.parent is None:
        return
    printSolutionStates(soln.parent)
    print(soln.moveMessage)


initFile = ""
goalFile = ""
outputFile = ""
mode = ""
start = puzzle()
end = puzzle()

if len(sys.argv) != 5:
    print("Usage: < initial state file > < goal state file > < mode > < output file >")
else:
    initFile = sys.argv[1]
    goalFile = sys.argv[2]
    outputFile = sys.argv[3]
    mode = sys.argv[4] 

readFile(initFile, start)
readFile(goalFile, end)
x = bfs(start, end)
printGame(x.State)
printSolutionStates(x)



