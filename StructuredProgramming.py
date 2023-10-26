from _codecs import utf_8_decode


class StructProgram:
    def __init__(self):
        pass

    def reverseInt(self, number):
        reverse = 0
        while number > 0:
            remainder = number % 10
            reverse = (reverse * 10) + remainder
            number = number // 10
        return reverse

    def factorial(self, number):
        result = 1
        for i in range(1, number + 1):
            result = result * i
        return result

    def bogenToGrad(self, rad):
        return (rad/3.14159) * 180

    def getMissingNumber(self, numberList):
        """finds missing number in a list of whole numbers from 0 to n"""
        fullList = list()
        for i in range(len(numberList) + 1):
            fullList.append(True)
        for j in range(len(numberList)):
            fullList[numberList[j]] = False
        for k in range(len(fullList)):
            if fullList[k]:
                return k

    def numberIsPalindrome(self, number):
        numberString = str(number)
        length = numberString.__len__()
        if length < 3:
            return True

        for i in range(length // 2):
            if int(numberString[i]) != int(numberString[length - 1 - i]):
                return False

        return True

    def numberIsPalindrome2(self, number):
        return number == self.reverseInt(number)

    def invertNumber(self, number):
        numberString = str(number)
        length = numberString.__len__()
        invertedString = ""
        for i in range(length):
            invertedString = invertedString + numberString[length - 1 - i]
        return invertedString

    def listTest(self, list):
        list[0] = 0

    def getNumberList(self, n):
        numberList = []
        while n != 0:
            if n % 3 == 0:
                n += 4
            if n % 4 == 0:
                n = n // 2
            if n % 4 != 0 and n % 3 != 0:
                n -= 1
            numberList.append(n)
        return numberList

    def yearIsLeapYear(self, year):
        if year % 4 == 0:
            if year % 100 == 0:
                if year % 400 == 0:
                    return True
                return False
            return True
        return False

    def clearScreen(self, amount):
        for i in range(amount):
            print()

    def printItemsInList(self, list):
        COIN_STRING = utf_8_decode(bytes([0xF0, 0x9F, 0xAA, 0x99]))[0]
        for i in range(len(list)):
            coinsStringAtIndex = ""
            for j in range(list[i]):
                coinsStringAtIndex = coinsStringAtIndex + f"{COIN_STRING}  "
            print(f"Row {i + 1}: {coinsStringAtIndex}")

    def enteredInputIsInRange(self, input, range):
        return input < range

    def removeIntAtIndex(self, list, index, amount):
        list[index] = list[index] - amount

    def runCoinGame(self):
        coinList = [5, 4, 3]
        isPlayerOneTurn = True
        QUESTION_ONE = "What row do you want to remove coins from?"
        QUESTION_TWO = "What amount of coins do you want to remove?"
        while sum(coinList) != 0:
            row = 0
            amount = 10
            while not self.enteredInputIsInRange(amount, coinList[row - 1] + 1):
                self.clearScreen(25)
                print(f"Player {1 if isPlayerOneTurn else 2}'s turn")
                self.printItemsInList(coinList)
                row = int(input(QUESTION_ONE))
                amount = int(input(QUESTION_TWO))
            self.removeIntAtIndex(coinList, row - 1, amount)
            isPlayerOneTurn = False if isPlayerOneTurn else True
        print(f"Player {2 if isPlayerOneTurn else 1} has won")





