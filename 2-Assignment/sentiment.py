
bag = ["is", "an", "excellent", "laptop", "No", "this", "not", "sarcasm"]

bag.sort(key=str.lower)


class review:
    good = 0
    text = ""
    words = []

x = review()

x.good = True
x.text = "This is an excellent laptop"
x.words = ["this", "is", "an", "excellent", "laptop"]

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

feats = []

featurize(x, bag, feats)

print(bag)
print(x.text)
printFeats(feats)






