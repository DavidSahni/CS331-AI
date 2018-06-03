from __future__ import print_function
import sys
import string
from string import punctuation
from classFile import *


okChars = string.ascii_letters + '1' + '0'



#takes a single review, the vocabulary, and the list of features(must be list object)
#makes a new feature for the review, appends to list of features
def featurize(rev, vocab, features):
    rev.words.sort(key=str.lower) #if not already

    feat = [0] * (len(vocab) +1)
    
    for i in range(len(rev.words)):
        if rev.words[i] in vocab:
            idx = vocab.index(rev.words[i])
            feat[idx] = 1

    feat[len(vocab)] = rev.good

    features.append(feat)

#prints a single features
def printFeature(feat):
    i = 0
    for i in range(len(feat)-1):
        print(feat[i], end=", ")
    print(feat[i+1])

#prints the entire list of features
def printFeats(features):
    for i in range(len(features)):
        printFeature(features[i])


def getVocab(trainFile, reviews):
    vocab = []
    filePtr = open(trainFile, 'r')
    data = filePtr.readlines()
    i = 0

    for i in range(len(data)):
        rev = Review()
        l = data[i].split()
        temp = []
        for s in l:
            x = ''
            for c in s: 
                if c in okChars:
                    x = x + c
                else:
                    continue
            temp.append(x)
        #l = [''.join(c for c in s if c not in string.punctuation) for s in l]
        l = temp
        while "0" in l:
            rev.good = 0
            l.remove("0")
        while "1" in l:
            rev.good = 1
            l.remove("1")
            
        l = [element.lower() for element in l]
        l = list(set(l))
        rev.words = sorted(l, key=str.lower)
        reviews.append(rev)
        vocab.extend(l)

    vocab = [element.lower() for element in vocab]
    vocab = list(set(vocab))
    filePtr.close()
    return sorted(vocab, key=str.lower)


def trainingPhase(ai):
    numGood = trainClass(ai)
    trainParams(ai, numGood)


def trainClass(ai):
    good = 0
    for x in ai.features:
        if x[len(x)-1] is 1:
            good += 1
    val = good/len(ai.features) #no dirichlet priors yet, just the class var
    ai.parentNode.cpt.append(val)
    return good

def trainParams(ai, numGood):
    numBad = len(ai.features) - numGood
    for i in range(len(ai.vocab)):
        word = ai.vocab[i]
        child = Node(word, ai.parentNode)
        tt = 0 #count for num records word = true class = true
        tf = 0 #count for num records word = true class = false
        for feat in ai.features:
            if feat[i] is 1:
                if feat[len(feat)-1] is 0:
                    tf += 1
                elif feat[len(feat)-1] is 1:
                    tt += 1
        ProbTT = (tt +1)/(numGood + len(ai.vocab))
        child.cpt.append(ProbTT)
        
        ProbTF = (tf + 1)/(numBad + len(ai.vocab))
        child.cpt.append(ProbTF)
        ai.parentNode.childNodes.append(child)




trainFile = ""
if len(sys.argv) != 3:
    print("Usage: classifier <trainfile> <testFile>")
    exit()
else:
    trainFile = sys.argv[1]
    testFile = sys.argv[2]

trainRev = []
testRev = []

trainVocab = getVocab(trainFile, trainRev)
getVocab(testFile, testRev) #put test file data into review objects but dont save the vocab

trainFeatures = []
testFeatures = []
for x in trainRev:
    featurize(x, trainVocab, trainFeatures)

for x in testRev:
    featurize(x, trainVocab, testFeatures)


classLabel = Node("CD")
ai = AI(classLabel, trainFeatures, trainVocab)
trainingPhase(ai)




#print(readFile(trainFile))
