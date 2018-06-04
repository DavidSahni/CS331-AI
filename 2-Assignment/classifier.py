from __future__ import print_function
from __future__ import division
import sys
import string
from string import punctuation
from classFile import *
import math

okChars = string.ascii_letters



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
        tabSep = data[i].split('\t')
        rev.good = int(tabSep[1].split()[0])
        l = tabSep[0].split()
        temp = []
        for s in l:
            x = ''
            for c in s:
                if c in okChars:
                    x = x + c
                else:
                    continue
            temp.append(x)
        l = temp

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
    ai.parentNode.wordTrueClassTrue = val
    ai.parentNode.wordTrueClassFalse = 1 - val
    return good

def trainParams(ai, numGood):
    numBad = len(ai.features) - numGood
    for i in range(len(ai.vocab)):
        word = ai.vocab[i]
        child = Node(word, ai.parentNode)
        ai.parentNode.childNodes.append(child)
        tt = 0 #count for num records word = true class = true
        tf = 0 #count for num records word = true class = false
        for feat in ai.features:
            if feat[i] is 1:
                if feat[len(feat)-1] is 0:
                    tf += 1
                elif feat[len(feat)-1] is 1:
                    tt += 1
        ProbTT = (tt +1)/(numGood + len(ai.vocab))
        child.wordTrueClassTrue = float(ProbTT)

        ProbTF = (tf + 1)/(numBad + len(ai.vocab))
        child.wordTrueClassFalse = float(ProbTF)


def testingPhase(ai, vocab):
    good = 0
    total = len(ai.features)
    for i in ai.features:
        if predict(i, vocab, ai) == i[len(i)-1]:
            good += 1
    accuracy = good / total
    print(accuracy)


def predict(feature, vocab, ai):
    i = 0
    j = 0
    prob1 = 0
    prob2 = 0
    for i in range(len(vocab)):
        n = ai.getNodeIdx(i)
        #print(feature[i])
        if feature[i] == 1:
            prob1 += math.log(float(n.getValues(True,True)))
            prob2 += math.log(float(n.getValues(True,False)))
        else:
            prob1 += math.log(float(n.getValues(False,True)))
            prob2 += math.log(float(n.getValues(False,False)))


    prob1 += math.log(n.parent.wordTrueClassTrue)
    prob2 += math.log(n.parent.wordTrueClassFalse)
    #print(prob2)
    if prob1 > prob2:
        return 1
    else:
        return 0



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
testingPhase(ai, trainVocab)
ai.features = testFeatures
testingPhase(ai, trainVocab)
