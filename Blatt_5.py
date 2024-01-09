from cmath import pi
from decimal import Decimal


def babylon(x):
    a = x
    i = 0
    while (a*a - x) > 0.001:
        a = (a + x / a) / 2
        i += 1
    return a, i


def babylon_revamped(x, precision):
    a = x
    i = 0
    while (a * a - x) > precision:
        a = (a + x / a) / 2
        i += 1
    return a, i


def babylon_revamped_v2(x, iterations):
    a = Decimal(x)
    i = 0
    for k in range(iterations):
        a = (a + x / a) / 2
        i += 1
    return a, i

print(babylon_revamped(5, 0.000000000000001))
print(babylon_revamped_v2(5, 100))


def is_whole_not_natural(number):
    return number < 0 and number % 1 == 0


def is_rational_not_whole(number):
    return number % 1 > 0

whole_num = -1
rational_not_whole = 1/10
real_not_rational = pi



