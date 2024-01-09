from math import gcd, sqrt, lcm

from colorama import Fore


def lowest_term(frac): # [a, b] = a/b
    numerator = frac[0]
    denominator = frac[1]
    g = gcd(numerator, denominator)
    return [numerator // g, denominator // g]


def invert_number(num):
    return num * -1


def lowest_term_revamped(frac):
    numerator = frac[0]
    denominator = frac[1]
    sign = numerator * denominator
    if (sign < 0 and denominator < 0) or (sign > 0 > numerator):
        denominator = invert_number(denominator)
        numerator = invert_number(numerator)
    g = gcd(numerator, denominator)
    return [numerator // g, denominator // g]


def multiply_terms(frac_a, frac_b):
    return lowest_term_revamped([frac_a[0] * frac_b[0], frac_a[1] * frac_b[1]])


def divide_terms(frac_a, frac_b):
    return lowest_term_revamped([frac_a[0] * frac_b[1], frac_a[1] * frac_b[0]])


def lcm_denominator_terms(frac_a, frac_b):
    frac_a = lowest_term_revamped(frac_a)
    frac_b = lowest_term_revamped(frac_b)
    lcm_denominators = lcm(frac_a[1], frac_b[1])
    lcm_multiplicator_a = lcm_denominators // frac_a[1]
    lcm_multiplicator_b = lcm_denominators // frac_b[1]
    return ([frac_a[0] * lcm_multiplicator_a, frac_a[1] * lcm_multiplicator_a],
            [frac_b[0] * lcm_multiplicator_b, frac_b[1] * lcm_multiplicator_b])


def subtract_terms(frac_a, frac_b):
    frac_a, frac_b = lcm_denominator_terms(frac_a, frac_b)
    return lowest_term_revamped([frac_a[0] - frac_b[0], frac_a[1]])


def get_rationals(a, b, n):
    # a < b
    diff = b - a

    step_size = diff / n
    result = []
    current_num = 0

    for i in range(n):
        current_num += step_size
        result.append(a + current_num)

    return result


def run_test_cases():
    TEST_CASES = [([1, -2], [-1, 2]),
                  ([-1, -2], [1, 2]),
                  ([-1, 2], [-1, 2]),
                  ([1, 2], [1, 2])]

    for test_case in TEST_CASES:
        print(Fore.LIGHTWHITE_EX)
        calc = lowest_term_revamped(test_case[0])

        if calc != test_case[1]:
            successful = False
        else:
            successful = True

        print(f"Test Case: {test_case[0]} | Calculated Value: {calc} | Expected Value: {test_case[1]}")
        print(Fore.GREEN + "Successful" if successful else Fore.RED + "Unsuccessful")


run_test_cases()

print(multiply_terms([1, 2], [50, 100]))
print(divide_terms([50, 100], [1, 4]))
print(lcm_denominator_terms([1, 10], [1, 25]))
print(subtract_terms([5, 10], [1, 4]))
result = get_rationals(7.9999, 8, 1000)
print(result[len(result) - 1])