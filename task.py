import math


def conv_num(num_str):
    digits = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4,
              '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
    hex_values = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4,
                  '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,
                  'a': 10, 'A': 10, 'b': 11, 'B': 11, 'c': 12, 'C': 12,
                  'd': 13, 'D': 13, 'e': 14, 'E': 14, 'f': 15, 'F': 15}

    num = 0
    decimal_points_count = 0
    neg_flag = 0
    hex_flag = 0

    if num_str[0] == '-':
        neg_flag = 1

    if '0x' in num_str or '0X' in num_str:
        hex_flag = 1

    for i in num_str:
        if i == '.':
            decimal_points_count += 1

    if decimal_points_count == 1:
        # string float
        dec_count = 0
        dec_flag = 0
        for char in num_str:
            if dec_flag:
                dec_count += 1
            if char == '.':
                dec_flag = 1
            if char in digits:
                num *= 10
                num = (num + digits[char])
        if neg_flag:
            return 0 - (num / (10 ** dec_count))
        else:
            return num / (10 ** dec_count)
    elif hex_flag:
        # string hex
        for i in range(len(num_str)):
            reverse_index = len(num_str) - i - 1
            char = num_str[reverse_index]
            if char == 'x' or char == 'X':
                if neg_flag:
                    return 0 - num
                else:
                    return num
            if char not in hex_values:
                return None
            num += (hex_values[char] * (16 ** i))
    else:
        # string integer
        for char in num_str:
            if char in digits:
                num *= 10
                num = (num + digits[char])
            else:
                if char != '-':
                    return None
        if neg_flag:
            return 0 - num
        else:
            return num


def my_datetime(num_sec):
    days_in_months = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30,
                      7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}
    days = math.floor(num_sec / 60 / 60 / 24)
    mm = 1
    dd = 1
    yyyy = 1970
    leap_year = 0
    while days >= 1:
        if yyyy % 4 == 0:
            if yyyy % 100 == 0:
                if yyyy % 400 == 0:
                    leap_year = 1
                else:
                    leap_year = 0
            else:
                leap_year = 1
        else:
            leap_year = 0

        if leap_year:
            if days >= 366:
                yyyy += 1
                days -= 366
            else:
                days_in_month = days_in_months[mm]
                if mm == 2:
                    days_in_month += 1
                if days > days_in_month:
                    days -= days_in_month
                    mm += 1
                else:
                    dd += days
                    days -= days
        else:
            if days >= 365:
                yyyy += 1
                days -= 365
            else:
                if days >= days_in_months[mm]:
                    days -= days_in_months[mm]
                    mm += 1
                else:
                    dd += days
                    days -= days
    return f"{mm:02}-{dd:02}-{yyyy}"


def conv_endian(num, endian='big'):
    hex_values = {0: '0', 1: '1', 2: '2', 3: '3', 4: '4',
                  5: '5', 6: '6', 7: '7', 8: '8', 9: '9',
                  10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F'}
    neg_flag = 0
    hex_count = 0
    hex_list = []
    hex_num = ''
    if num < 0:
        neg_flag = 1
        num = 0 - num
    while num >= (16 ** hex_count):
        hex_count += 1
    # calculate hex values
    for i in range(hex_count + 1):
        exponent = hex_count - i
        quotient = num // (16 ** exponent)
        hex_list.append(hex_values[quotient])
        num -= (quotient * (16 ** exponent))
    # format hex values into a string
    if endian == 'big':
        for j in range(len(hex_list)):
            hex_num += hex_list[j]
            if j % 2 == 1 and j != (len(hex_list) - 1):
                hex_num += ' '
        if neg_flag:
            return '-' + hex_num
        else:
            return hex_num
    elif endian == 'little':
        pair = ''
        for k in range(len(hex_list)):
            pair += hex_list[k]
            if k % 2 == 1:
                hex_num = pair + hex_num
                pair = ''
                if k != (len(hex_list) - 1):
                    hex_num = ' ' + hex_num
        if neg_flag:
            return '-' + hex_num
        else:
            return hex_num
    else:
        return None
