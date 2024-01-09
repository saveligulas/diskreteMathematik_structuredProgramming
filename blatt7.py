from fractions import Fraction


def set_product(A, B):
    result = set()
    for a in A:
        for b in B:
            result.add((a, b))
    return result


def set_union(A, B):
    result = set()
    for a in A:
        result.add(a)

    for b in B:
        if b not in result:
            result.add(b)
    return result


def set_intersection(A, B):
    result = set()
    for a in A:
        for b in B:
            if a == b:
                result.add(a)
    return result


def set_difference(A, B):
    result = set()
    for a in A:
        if a not in B:
            result.add(a)
    return result


A = set(range(5))
B = set(range(3,8))


def get_set_a(maximum, as_tuple=False):
    if as_tuple:
        return {(1, element) for element in range(1, maximum + 1)}
    return {1 / element for element in range(1, maximum + 1)}


def get_set_b(maximum):
    return {1 * (2 ** element) for element in range(0, maximum + 1)}


def get_set_c(amount=100):
    return {((-1) ** element) * (element ** 3) for element in range(1, amount + 1)}


def get_next_even_natural_num(num=2):
    while True:
        yield num
        yield from get_next_even_natural_num(num + 2)


def rat_revamped():
    c = 2
    unique_generated_fractions = set()
    while True:
        den = 1
        while den < c:
            fraction = Fraction(c - den, den)
            if fraction not in unique_generated_fractions:
                yield Fraction(c - den, den)
                unique_generated_fractions.add(fraction)
            den += 1
        c +=1


def Rat():
    c = 2
    while True:
        den = 1
        while den < c:
            yield Fraction(c - den, den)
            den += 1
        c +=1


def viewGen(gen, n):
    c = 1
    L = []
    for x in gen:
        if c > n:
            break
        L.append(x)
        c +=1
    return L


print(viewGen(get_next_even_natural_num(), 50))
for q in viewGen(Rat(), 10):
    print(q)