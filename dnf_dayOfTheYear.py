from colorama import Fore


def is_leap_year(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            return False
        return True
    return False


def get_day_of_the_year(day, month, year):
    MONTH_DICT = {'Jan': (1, 31),
                  'Feb': (2, 28),
                  'Mar': (3, 31),
                  'Apr': (4, 30),
                  'May': (5, 31),
                  'Jun': (6, 30),
                  'Jul': (7, 31),
                  'Aug': (8, 31),
                  'Sep': (9, 30),
                  'Oct': (10, 31),
                  'Nov': (11, 30),
                  'Dec': (12, 31)}
    ERR_MSG = 'ERR'
    MONTH_DAYS = []
    for key in MONTH_DICT.keys():
        MONTH_DAYS.append(MONTH_DICT.get(key))
    day_calc = 0

    if type(year) != int or 1 > year:
        return ERR_MSG

    LEAP_YEAR = is_leap_year(year)

    if type(month) != str or month not in MONTH_DICT.keys():
        return ERR_MSG

    MONTH = MONTH_DICT.get(month)[0]

    additive = 0
    if LEAP_YEAR:
        if MONTH == 2:
            additive += 1
        if MONTH > 2:
            day_calc += 1

    if type(day) != int or MONTH_DICT.get(month)[1] + additive < day or day < 1:
        return ERR_MSG

    for i in range(1, MONTH):
        days = 0

        for pair in MONTH_DAYS:
            if i == pair[0]:
                days = pair[1]
                break

        day_calc += days

    return day_calc + day


def run_test_cases():
    ERR = 'ERR'
    TEST_CASES = [(31, 'Apr', 1900, ERR),
                  (29, 'Feb', 2023, ERR),
                  (4, 'Test', 2023, ERR),
                  (29, 'Feb', 1800, ERR),
                  (10, 'Nov', 2023, 314),
                  (29, 'Feb', 2024, 60),
                  (10, 'Nov', 2024, 315),
                  (29, 'Feb', 2000, 60),
                  (31, 'Dec', 2023, 365)]

    for test_case in TEST_CASES:
        print(Fore.LIGHTWHITE_EX)
        calc = get_day_of_the_year(test_case[0], test_case[1], test_case[2])

        if calc != test_case[3]:
            successful = False
        else:
            successful = True

        print(f"Test Case: Day-{test_case[0]}, Month-{test_case[1]}, Year-{test_case[2]} \nExpected Value: {test_case[3]} | Calculated Value: {calc}")
        print(Fore.GREEN + "Successful" if successful else Fore.RED + "Unsuccessful")


run_test_cases()


