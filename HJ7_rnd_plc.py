# truncate number by decimals
input_num = round(float(input('Enter a Number:')), 5)
input_str_int = str(input_num).split('.')[0]
input_str_float = str(input_num).split('.')[1]

if float('0.'+input_str_float) >= 0.5:
    result = int(input_str_int) + 1
    print(result)
    
else:
    result = int(input_str_int)
    print(result)