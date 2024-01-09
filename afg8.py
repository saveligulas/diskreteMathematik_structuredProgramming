# all schaut, ob alle Werte den Wahrheitswert true haben
all([True, False, True])


# prüften ob ein Argument nur tupel enthält
def onlyTuples(s):
    return (all(map(lambda x: type(x) is tuple, s)))

# ist eine Menge von Tupeln "rechtseindeutig"?
def rightUnique(f):
    for x1, y1 in f:
        for x2, y2 in f:
            if x1 == x2 and y1 != y2:
                return False
    return True
rightUnique([(1,2), (2,4), (1,3)])


def isFunction(f):
    return onlyTuples(f) and rightUnique(f)


isFunction([(1, 2), (2, 4), (3, 2)])