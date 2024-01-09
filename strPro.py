def number_row_development(num, z):
    result = 1
    faculty = 1
    for i in range(num - 1):
        exp_fac = 1 + i
        result += (z ** exp_fac) / faculty * exp_fac
        faculty *= exp_fac
    return result


print(number_row_development(5, 5))


def kgv(a, b):
    a_placeholder = a
    b_placeholder = b
    while a != b:
        if a < b:
            a += a_placeholder
        else:
            b += b_placeholder
    return a


print(kgv(10, 25))


class Coordinate:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Rectangle:
    def __init__(self, bottom_left_corner, height, width):
        self.starting_point_bottom_left : Coordinate = bottom_left_corner
        self.height = height
        self.width = width


