import math

def distance(p1, p2):
    x1 = p1[0]
    y1 = p1[1]
    x2 = p2[0]
    y2 = p2[1]

    return math.sqrt(math.pow((x2 - x1), 2) + math.pow((y2 - y1), 2))

def getS(p1, p2):
    x1 = p1[0]
    x2 = p2[0]
    return abs(x2 - x1)

def getG(p1, p2):
    y1 = p1[1]
    y2 = p2[1]
    return abs(y2 - y1)