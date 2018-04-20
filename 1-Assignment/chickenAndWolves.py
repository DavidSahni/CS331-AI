from classFile import *
from collections import deque
import heapq
import sys
import itertools

itr = itertools.count()
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

#iterative deeping depth first search, takes in start state and end state
def iddfs(start, goal):
    closed = {}
    startNode = Node(None, start)
    fringe = deque([startNode])
    dlimit = 1
    maxDepth = 1500
    while True:
        counter = 0
        while True:
            if len(fringe) < 1:
                break
            node = fringe.pop()
            if isPuzzleEqual(node.State, goal) is True:
                printSolutionStates(node, True)
                printSolutionStates(node, False)
                print('expanded:', counter, "nodes")
                print(node.depth, 'nodes on solution path')
                return node
            else:
                if node.depth < dlimit: #only expand the node if its depth is less than limit
                    # if inClosed(closed, node.State) is False:
                    counter += 1
                        # addClosed(closed, node.State)
                    fringe.extend(expandDfs(node))
        dlimit = (dlimit * 2) + 1
        fringe = deque([startNode])
        closed = {}
        if dlimit > maxDepth:
            print('No Solution found in Max Depth Limit')
            return

#depth first search, takes in start state and end state
def dfs(start, goal):
    closed = {}
    startNode = Node(None, start)
    fringe = deque([startNode])
    counter = 0
    while True:
        if len(fringe) < 1:
            return None
        node = fringe.pop()
        if isPuzzleEqual(node.State, goal) is True:
            printSolutionStates(node, True)
            printSolutionStates(node, False)
            print('expanded:', counter, "nodes")
            print(node.depth, 'nodes on solution path')
            return node
        else:
            if inClosed(closed, node.State) is False:
                counter += 1
                addClosed(closed, node.State)
                fringe.extend(expandDfs(node))

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
            printSolutionStates(node, True)
            printSolutionStates(node, False)
            print('expanded:', counter, "nodes")
            print(node.depth, 'nodes on solution path')
            return node
        else:
            if inClosed(closed, node.State) is False:
                counter += 1
                addClosed(closed, node.State)
                fringe.extend(expandBfs(node))

#expansion for breadth first search
#just keeps it as a fifo stack
def expandBfs(node):
    succesors = []
    generateSuccesors(succesors, node)
    for x in succesors:
        x.depth = node.depth + 1
    return succesors

def expandDfs(node):
    succesors = []
    generateSuccesors(succesors, node)
    for x in succesors:
        x.depth = node.depth + 1
    succesors.reverse() #since we are extending right and popping off end, need to put the first action first
    return succesors

#generates succesors for a state and puts them in succesor object
def generateSuccesors(succesors, node):
    state = node.State
    global itr
    if state.isMoveValid(1, 0):
        x = state.copyToNew()
        x.moveAnimals(1, 0)
        newNode = Node(node, x)
        newNode.pathCost = node.pathCost + 1
        newNode.orderCount = next(itr)
        succesors.append(newNode)

    if state.isMoveValid(2, 0):
        x = state.copyToNew()
        x.moveAnimals(2, 0)
        newNode = Node(node, x)
        newNode.pathCost = node.pathCost + 1
        newNode.orderCount = next(itr)
        succesors.append(newNode)

    if state.isMoveValid(0, 1):
        x = state.copyToNew()
        x.moveAnimals(0, 1)
        newNode = Node(node, x)
        newNode.pathCost = node.pathCost + 1
        newNode.orderCount = next(itr)
        succesors.append(newNode)

    if state.isMoveValid(1, 1):
        x = state.copyToNew()
        x.moveAnimals(1, 1)
        newNode = Node(node, x)
        newNode.pathCost = node.pathCost + 1
        newNode.orderCount = next(itr)
        succesors.append(newNode)
        
    if state.isMoveValid(0, 2):
        x = state.copyToNew()
        x.moveAnimals(0, 2)
        newNode = Node(node, x)
        newNode.pathCost = node.pathCost + 1
        newNode.orderCount = next(itr)       
        succesors.append(newNode)

#checks if a state is in the closed set
def inClosed(closed, target):
    inSet = False
    for i in closed.keys():
        if isPuzzleEqual(target, closed[i]) is True:
            inSet = True
            break
    return inSet

#adds a new entry to the closed set
def addClosed(closed, state):
    i = len(closed)
    closed[i] = state

#recursively prints the moves, soln is a node object
def printSolutionStates(soln, output):
    if soln.parent is None:
        return
    printSolutionStates(soln.parent, output)
    if output is False:
        soln.State.printState()
    elif output is True:
        soln.State.printStateToFile(outputFile)


def aStarSearch(start, goal):
    goalBank = goal.boatBank
    closed = {}
    startNode = Node(None, start)
    startNode.pathCost = 0 #root!
    fringe = []
    heapq.heappush(fringe,(0,0, startNode))
    counter = 0
    while True:
        if len(fringe) < 1:
            return None
        tup = heapq.heappop(fringe)
        node = tup[2]
        if isPuzzleEqual(node.State, goal) is True:
            printSolutionStates(node, True)
            printSolutionStates(node, False)
            print('expanded:', counter, "nodes")
            print(node.depth, 'nodes on solution path')
            return node
        else:
            if inClosed(closed, node.State) is False:
                counter += 1
                addClosed(closed, node.State)
                expandAstr(fringe, node, goalBank)

def expandAstr(fringe, node, goalBank):
    succesors = []
    generateSuccesors(succesors, node)
    addSuccesors(fringe, succesors, goalBank, node)
    for x in succesors:
        x.depth = node.depth + 1
    #return succesors

def addSuccesors(fringe, succs, goalBank, node):
    for newNode in succs:
        g = newNode.pathCost
        h = heuristic(newNode, goalBank, node)
        f = g + h
        #print("Priority info:", f, newNode.orderCount, g)
        heapq.heappush(fringe, (f, newNode.orderCount, newNode))

def heuristic(newnode, goalBank, Parent):
    #this heuristic simplifies the game to just moving generic animals from one side to another following
    #the rule the river cannot be crossed without 1 animal
    #this heuristic ignores the wolves > chickens invalidity
    state = newnode.State
    if goalBank == Parent.State.boatBank: #this means we are going back to get more, higher priority on moving 1 animal
        if state.numMoved == 1:
            return 1
        else:
            return 2
    elif goalBank != Parent.State.boatBank: #we are going to the goal bank, send as many as possible!
        if state.numMoved == 2:
            return 1
        else:
            return 2

initFile = ""
goalFile = ""
outputFile = ""
mode = ""
start = puzzle()
end = puzzle()

if len(sys.argv) != 5:
    print("Usage: < initial state file > < goal state file > < mode > < output file >")
    exit()
else:
    initFile = sys.argv[1]
    goalFile = sys.argv[2]
    mode = sys.argv[3]
    outputFile = sys.argv[4]

readFile(initFile, start)
readFile(goalFile, end)
printGame(start)


x = Node(None, None)
if mode == 'bfs':
    x = bfs(start, end)
elif mode == 'dfs':
    x = dfs(start, end)
elif mode == 'iddfs':
    x = iddfs(start, end)
elif mode == 'astar':
    x = aStarSearch(start, end)
else:
    print('Incorrect Mode!')
    exit()
