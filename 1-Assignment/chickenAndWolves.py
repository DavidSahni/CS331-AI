from classFile import puzzle
import sys


def readInitial(initFile, game):
    filePtr = open(initFile, 'r')
    data = filePtr.readline()
    leftSide = data.split(',')
    game.chickensLeft = leftSide[0]
    game.wolvesLeft = leftSide[1]
    game.boatBank = leftSide[2]

    data = filePtr.readline()
    filePtr.close()
    rightSide = data.split(',')
    game.chickensRight = rightSide[0]
    game.wolvesRight = rightSide[1]

def printGame(game):
    print("Left Side Counts:")
    print("Chickens: ", game.chickensLeft)
    print("Wolves: ", game.wolvesLeft)
    print("Right Side Counts:")
    print("Chickens: ", game.chickensRight)
    print("Wolves: ", game.wolvesRight)
    game.printBoat()


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

readInitial(initFile, start)
printGame(start)



