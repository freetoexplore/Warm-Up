# concating result by digit place with 16**i
# 0x: Hex digit

input_str = str(input())

if input_str[:2] == '0x':
    input_int = input_str[2:]

hex_dict = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, 'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15}

if input_str[:2] == '0x':
    input_int = input_str[2:]
    
result = 0
for i in range(len(input_int)):
    
    # without multiple by 16 at the last digit
    if i == 0:
        letter = input_int[-1]
        result += (hex_dict[letter])
        # print('**', letter)
    
    # multiply by 16 in the rest digit(s)
    elif i > 0:
        letter = input_int[-1*(i + 1)]
        result += 16**i * hex_dict[letter] 
        # print('*****', letter)

print(result)