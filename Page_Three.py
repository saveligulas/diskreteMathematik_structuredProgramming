def russian_farmer_multiplication(a, b):
    half_list = []
    double_list = []
    sum = 0
    multiplicand = a
    multiplicator = b

    while multiplicand > 0:
        half_list.append(multiplicand)
        multiplicand = multiplicand // 2

    for i in range(len(half_list)):
        double_list.append(multiplicator)

        if half_list[i] % 2 != 0:
            sum += double_list[i]

        multiplicator = multiplicator * 2

    return sum


def is_leap_year(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            return False
        return True
    return False


def get_message(d, m, y, sum):
    return f"The {d} of {m}, is the {sum} day of the year {y}"


def day_in_the_year(day, month, year):
    ERR_MSG = "ERR"
    MONTH_DICT = {1: ('January', 31),
                  2: ('February', 28),
                  3: ('March', 31),
                  4: ('April', 30),
                  5: ('May', 31),
                  6: ('June', 30),
                  7: ('July', 31),
                  8: ('August', 31),
                  9: ('September', 30),
                  10: ('October', 31),
                  11: ('November', 30),
                  12: ('December', 31)}

    MONTH_STRING_INT_DICT = {'Jan': 1,
                             'Feb': 2,
                             'Mar': 3,
                             'Apr': 4,
                             'May': 5,
                             'Jun': 6,
                             'Jul': 7,
                             'Aug': 8}

    if type(day) != int or type(year) != int or (type(month) != int or month not in MONTH_STRING_INT_DICT.keys()):
        return ERR_MSG

    leap_year = is_leap_year(year)
    day_string = ERR_MSG
    month_string = ERR_MSG
    year_string = ERR_MSG

    day_calc = 0

    if year > - 1:
        year_string = str(year)
    else:
        return ERR_MSG

    if month in MONTH_DICT.keys():
        month_string = MONTH_DICT.get(month)[0]
    else:
        return ERR_MSG

    add = 1

    if month_string == MONTH_DICT.get(2)[0] and leap_year:
        add += 1

    if day in range(1, MONTH_DICT.get(month)[1] + add):
        day_string = str(day)
        day_calc += day
    else:
        return ERR_MSG

    for i in range(1, month):
        day_calc += MONTH_DICT.get(i)[1]

    if leap_year and month > 2:
        day_calc += 1

    return get_message(day_string, month_string, year_string, day_calc)


def local_min_max(number_list):
    prev_num = 0
    next_num = 0
    current_num = 0

    local_mins = 0
    local_maxs = 0

    for i in range(len(number_list)):
        if 0 < i < len(number_list) - 1:
            prev_num = number_list[i - 1]
            next_num = number_list[i + 1]
            current_num = number_list[i]

            if prev_num > current_num and next_num > current_num:
                local_mins += 1

            if prev_num < current_num and next_num < current_num:
                local_maxs += 1

    return local_mins, local_maxs


def get_arithmetic_info(number_list):
    max = number_list[0]
    min = number_list[0]
    count = 0

    for i in range(len(number_list)):
        current_num = int(number_list[i])
        count += current_num

        if min > current_num:
            min = current_num

        if max < current_num:
            max = current_num

    return min, max, count // len(number_list)


def get_freq_of_most_common(number_list):
    prev_num = number_list[0]
    dict = {prev_num : 1}

    for i in range(len(number_list)):
        current_num = number_list[i]

        if i > 0:
            if prev_num != current_num:
                dict[current_num] = 1
            else:
                dict[current_num] = dict.get(current_num) + 1

            prev_num = current_num

    max_amount = 0
    num = 0

    for key in dict.keys():
        if dict.get(key) > max_amount:
            max_amount = dict.get(key)
            num = key

    return num, max_amount


def count_words(text):
    count = 0
    word_has_started = False

    for i in range(len(text)):
        if not word_has_started:
            if text[i].isalpha():
                word_has_started = True
        else:
            if not text[i].isalpha() or i == len(text) - 1:
                word_has_started = False
                count += 1

    return count

print(count_words("   test.!=      i like, this"))
print(day_in_the_year(29, 2, 1900))
print(local_min_max([1, 3, 5, 4, 6, 5, 1, 2, 1, 1]))
print(get_arithmetic_info([1, 3, 5, 4, 6, 5, 1, 2, 1, 1]))
print(get_freq_of_most_common([1,1,1,1,1,1,2,2,2,2,2,2,2,2,2,3,3,3,3,3,3,3,3,3]))
