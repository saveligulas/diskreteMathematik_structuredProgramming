def only_tuple(s):
    return all(map(lambda x: type(x) is tuple, s))


def right_unique(f):
    for x1, y1 in f:
        for x2, y2 in f:
            if x1 == x2 and y1 != y2:
                return False
    return True


def is_function(f):
    return only_two_tuples(f) and right_unique(f)


def is_two_tuple(t):
    return len(t) == 2


def only_two_tuples(t):
    return all(map(lambda x: is_two_tuple(x), t))


def is_injective(f):
    target_set = set()
    for pair in f:
        if pair[1] in target_set:
            return False
        target_set.add(pair[1])
    return True


def comp(f, g):
    result = set()
    for pair in f:
        for pair2 in g:
            if pair[1] == pair2[0]:
                result.add((pair[0], pair2[1]))
    return result


print(only_two_tuples({(0, 2), (0, 3, 5)}))
print(is_function({(7, 6), (7, 8)}))
print(is_function({(6, 5, 3)}))
print(comp({(1, 2), (2, 3)}, {(2, 10), (3, 5)}))
