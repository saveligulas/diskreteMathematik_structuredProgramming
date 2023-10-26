import string

import null


class BinaryDecimalCalculator:
    def __init__(self):
        return

    def binToDecimal(self, binary):
        decimal = 0
        length = str(binary).__len__()
        for i in range(length):
            decimal += int(str(binary)[i]) * (2 ** (length - 1 - i))
        return decimal

    def decimalToBin(self, decimal):
        counter = 0
        division = decimal
        binary = 0
        while division != 0:
            modulo = division % 2
            division = division // 2
            binary += modulo * (10 ** counter)
            counter += 1
        return binary

    def decToOcta(self, decimal):
        count = 0
        division = decimal
        octa = 0
        while division != 0:
            modulo = division % 8
            division = division // 8
            octa += modulo * (10 ** count)
            count += 1
        return octa

    def octaToDecimal(self, octa):
        decimal = 0
        length = str(octa).__len__()
        for i in range(length):
            decimal += int(str(octa)[i]) * (8 ** (length - 1 - i))
        return decimal

    def baseToDecimal(self, number, base):
        if base > 36 or any(char.isalnum() for char in str(number)):
            return "Function can only handle numbers up to base-36"
        decimal = 0
        length = str(number).__len__()
        number = number.lower()
        if any(char.isalpha() for char in str(number)):
            decimal = self.baseHigherthanTenToDecimal(number, base, length)
        else:
            for i in range(length):
                decimal += int(str(number)[i]) * (base ** (length - 1 - i))
        return decimal

    def hexToDecimal(self, hexa):
        hexa = hexa.lower()
        decimal = 0
        length = str(hexa).__len__()
        for i in range(length):
            chiffre = str(hexa)[i]
            if chiffre.isdigit():
                pass
            else:
                chiffre = 10 + string.ascii_lowercase.index(chiffre)
            decimal += int(chiffre) * (16 ** (length - 1 - i))
        return decimal

    def baseHigherthanTenToDecimal(self, number, base, length):
        decimal = 0
        for i in range(length):
            chiffre = str(number)[i]
            if chiffre.isdigit():
                pass
            else:
                chiffre = 10 + string.ascii_lowercase.index(chiffre)
            decimal += int(chiffre) * (base ** (length - 1 - i))
        return decimal

    def convertDecimalToBase(self, decimal, base):
        counter = 1
        division = decimal // base
        first_digit = decimal % base
        if first_digit >= 10:
            result = self.convertNumbertoChar(first_digit)
        else:
            result = str(first_digit)
        while division != 0:
            modulo = division % base
            division = division // base
            if modulo >= 10:
                result = self.convertNumbertoChar(modulo) + result
            else:
                result = str(modulo) + result
            counter += 1
        return result

    def convertNumbertoChar(self, number):
        return chr(ord('a') + number - 10)

    def convertListToString(self, list):
        return ''.join(map(str, list))

    def multiplyBitByFourteen(self, binary):
        return (binary << 1) + (binary << 2) + (binary << 3)

    def productInXBit(self, numberOne, numberTwo, bits):
        product = numberOne * numberTwo
        bitProduct = ""
        counter = bits
        while counter != 0:
            bitProduct = str(product % 2) + bitProduct
            product = product // 2
            counter -= 1
        return bitProduct