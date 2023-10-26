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

def ggT(a, b):
    counter = 1
    while a - b != 0:
        if a > b:
            a = a - b
        else:
            b = b - a
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

print(extggT(400, 225))