import sys
import string
from string import punctuation
from classFile import *

def readFile(trainFile):
    filePtr = open(trainFile, 'r')
    data = filePtr.readline()
    rev = Review()
    l = data.split()
    l = [''.join(c for c in s if c not in string.punctuation) for s in l]
    while "0" in l:
        rev.good = 0
        l.remove("0")
    while "1" in l:
        rev.good = 1
        l.remove("1")

    l = [element.lower() for element in l]
    l = list(set(l))
    return sorted(l, key=str.lower)

def getVocab(trainFile):
    vocab = []
    filePtr = open(trainFile, 'r')
    data = filePtr.readlines()
    i = 0

    for i in range(len(data)):
        vocab.extend(data[i].split())

    vocab = [''.join(c for c in s if c not in string.punctuation) for s in vocab]
    while "0" in vocab:
            vocab.remove("0")
    while "1" in vocab:
            vocab.remove("1")

    vocab = [element.lower() for element in vocab]
    vocab = list(set(vocab))
    return sorted(vocab, key=str.lower)

trainFile = ""

if len(sys.argv) != 2:
    print("Usage: classifier <file>")
    exit()
else:
    trainFile = sys.argv[1]

print getVocab(trainFile)
print readFile(trainFile)
