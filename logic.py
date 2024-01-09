def conjunction(a, b):
    ret_val = False
    if a:
        ret_val = True
    if b:
        ret_val = True
    return ret_val


def negation(a):
    if a:
        return False
    else:
        return True


def implication(a, b):
    if a:
        if b:
            return True
        return False
    else:
        return True


def equivalent(a, b):
    if a:
        if b:
            return True
    else:
        if b:
            return True
    return False


def get_truth_table():
    vals = []
    for i in (True, False):
        for j in (True, False):
            vals.append((i, j))
    return vals


def get_truth_table_three():
    vals = []
    for i in (True, False):
        for j in (True, False):
            for k in (True, False):
                vals.append((i, j, k))
    return vals


table_two = get_truth_table()
table_three = get_truth_table_three()


def a_one(a, b, c):
    return a and (b or c)


def a_two(a, b, c):
    return (a and b) or (a and c)


def b_one(a, b):
    return not (a and b)


def b_two(a, b):
    return (not a) or (not b)

print("Aufgabe a")
for val in table_three:
    print(f"P: {val[0]} | Q: {val[1]} | R: {val[2]} - {a_one(val[0], val[1], val[2]) == a_two(val[0], val[1], val[2])}")

print()
print("Aufgabe b")
for val in table_two:
    print(f"P: {val[0]} | Q: {val[1]} - {b_one(val[0], val[1]) == b_two(val[0], val[1])}")