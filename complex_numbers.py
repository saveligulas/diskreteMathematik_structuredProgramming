import numpy


def complex_subtract(a, b, c, d):
    real_result = a - c
    imaginary_result = b - d
    return complex(real_result, imaginary_result)


def complex_multiply(a, b, c, d):
    real_result = a * c
    imaginary_result_square = -(b * d)
    imaginary_result = (a * d + b * c)
    return complex(real_result + imaginary_result_square, imaginary_result)


def complex_divide(a, b, c, d):
    numerator = complex_multiply(a, b, c, -1 * d)
    denominator = complex_multiply(c, d, c, -1 * d)
    return numerator, denominator


def complex_conjugate(a, b):
    return complex(a, b * -1)


print(3 - 1j - 5 - 0j)
print(complex_subtract(3, -1, 5, 0))
print((1 + 1j) * (2 - 2j))
print(complex_multiply(1, 1, 2, -2))
print(numpy.conjugate(3 - 10j))
print(complex_conjugate(3, -10))
print(complex_divide(2,3,2,-2))