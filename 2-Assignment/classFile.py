
class Review:
    good = 0
    words = []


class Node:
    name = ""
    parent = None
    childNodes = []
    #P(M|D) ordered [(m=t d=t), (m=t d=f)]
    cpt = (0, 0)

    def __init__(self, name, parentNode=None):
        self.parent = parentNode
        self.name = name


class AI:
    parentNode = None
    features = None
    vocab = None

    def __init__(self, parentNode, features, vocab):
        self.parentNode = parentNode
        self.features = features
        self.vocab = vocab

    def findWord(self, word):
        return self.vocab.index(word)

    def getNode(self, word):
        i = self.findWord(word)
        return self.parentNode.childNodes[i]

