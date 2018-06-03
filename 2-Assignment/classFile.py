
class Review:
    good = 0
    words = []


class Node:
    parent = None
    child = []
    #P(M|D) ordered [(m=t d=t), (m=t d=f), (m=f d=t), (m=f d=f)]
    cpt = []

