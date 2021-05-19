def my_func():
    return "Hello World"

def conv_num(num_str):
    digits = {'0':0, '1':1, '2':2, '3':3,'4':4,
              '5':5, '6':6, '7':7,'8':8, '9':9}
    hex_values = {'0':0, '1':1, '2':2, '3':3, '4':4,
                  '5':5, '6':6, '7':7, '8':8, '9':9, 
                  'a':10, 'A':10, 'b':11, 'B':11, 'c':12, 'C':12,
                  'd':13, 'D':13, 'e':14, 'E':14, 'f':15, 'F':15}
    
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
        #string float
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
        #string hex
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
        #string integer
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
            
