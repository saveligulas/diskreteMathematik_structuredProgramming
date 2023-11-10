def factorial(n):
    result = 1
    n = int(n)
    while n > 0:
        result = result * n
        n -= 1
    return result

inputNumber = input("Enter a number: ")

print(f"Die Faktorielle der Zahl {inputNumber} ist: {factorial(inputNumber)}")