import math
from datetime import time
from timeit import timeit

import timer


def sumMod(a, b, rkr):
    return (a + b) % rkr

def crossSum(number):
    sum = 0
    while number > 0:
        sum += number % 10
        number = number // 10
    return sum

def iteratedCrossSum(number):
    iteratedSum = crossSum(number)
    while iteratedSum % 10 != iteratedSum:
        iteratedSum = crossSum(iteratedSum)
    return iteratedSum

def addInv2(number, rkr):
    calc = number % rkr
    return rkr - calc


def naive_ggT(a, b):
    num = a if a < b else b
    result = 0
    while result == 0:
        num -= 1
        if a % num == 0 and b % num == 0:
            result = num
    return result


def ggT(a, b):
    while a - b != 0:
        if a > b:
            a = a - b
        else:
            b = b - a
    return a


def ggT_better(a, b):
    while b != 0:
        temp = a % b
        a = b
        b = temp
    return a


def extggT(a, b):
    dict = {a : str(a), b : str(b)}
    numbers = [a, b]
    calc = []
    steps = 0
    while a - b != 0:
        if a > b:
            placeholder = a
            a = a - b
            if a != b:
                dict[a] = f"{placeholder}-{b}"
            numbers.append(a)
            calc.append((placeholder, b))
        else:
            placeholder = b
            b = b - a
            if a != b:
                dict[b] = f"{placeholder}-{a}"
            numbers.append(b)
            calc.append((placeholder, a))
        steps += 1

    term = str(a)

    for i in range(len(calc)):
        index = len(calc) - 1 - i
        number_strings = term.split("-")
        for num in number_strings:
            term = term.replace(num, f"{calc[index][0]}-{calc[index][1]}")
    return term


def checkISBN(digits):
    counter = 0
    sum = 0
    for d in digits:
        if counter == 9:
            return (sum % 11) == int(d)
        if d.isdigit():
            counter += 1
            sum += int(d) * counter


def isPrime(n):
    for i in range(2, math.floor(math.sqrt(n))):
        if (n % i) == 0:
            return False
    return True

def getPrimes(n):
    """Returns a list of prime numbers in between 2 and n (inclusive)"""
    primes = []
    for i in range(2, n + 1):
        if isPrime(i):
            primes.append(i)
    return primes


def getSieb(n):
    primes = list(range(1, n + 1))
    sum = 0

    for i in range(2, math.floor(math.sqrt(n))):
        if (isPrime(i)):
            counter = 2
            while (sum < n):
                sum = i * counter
                counter += 1
                if (sum in primes):
                    primes.remove(sum)

    return primes


def pzSieb(n):
    primes = []
    numbers = list(range(2,n))
    c = 2
    while c*c < n:
        for k in range(c, n , c):
            if k in numbers:
                numbers.remove(k)
        primes.append(c)
        c = numbers[0]
    return [1] + primes + numbers


def primeFactor(n):
    result = []
    c = 2
    while n > 1:
        while True:
            if n % c == 0:
                result.append(c)
                n //= c
                break
            c += 1
    return result


def convertNumberToChar(n):
    return chr(ord('a') + n)


def caesarEnc(msg, key):
    result = ""
    for char in msg:
        result += (chr(ord(char) - ord('a') + key % 26 + ord('a')))
    return result


print(primeFactor(32592))
print(convertNumberToChar(0))
print(caesarEnc("Hallo", 5))
print(pzSieb(1000)[50])