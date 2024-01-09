import functools
from functools import *


def fibonacci_iterative(n):
    if n <= 1:
        return n
    else:
        num = [0, 1]
        for i in range(2, n + 1):
            num.append(num[i - 2] + num[i - 1])
        return num[-1]


def fibonacci_recursive(n, i=2, num=[0, 1]):
    if n <= 1:
        return n
    if i == n + 1:
        print(num)
        return num[-1]
    num.append(num[i - 2] + num[i - 1])
    return fibonacci_recursive(n, i + 1, num)


print(fibonacci_iterative(6))
print(fibonacci_recursive(15))
