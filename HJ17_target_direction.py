import re

# dictionary for reference, not used in case by 2023/4/29
direction_dict = {'A': 'l -1', 'D': 'r 1', 'W': 'u 1', 'S': 'd -1'}

input_str = [_ for _ in str(input()).split(';')]
output = [0, 0]

for _ in input_str:

# check if alphabetic letters are in wrong place, i.e., end of string    
    letter_test = str(re.search(r'[a-z]', _[1:3].lower()))
    
    # check if step units are in acceptable range
    if len(_) >= 2 and len(_) <= 3 and letter_test == 'None' and int(_[1:3]) >= -99 and int(_[1:3]) <= 99 :
        units = int(_[1:3])
        
        if _[0] == 'A':
            output[0] -= units
            
        elif _[0] == 'D':
            output[0] += units
            
        elif _[0] == 'W':
            output[1] += units
            
        elif _[0] == 'S':
            output[1] -= units
            
        else:
            output = output
    
    else:
        output = output

# append final output in a string
result= str(output[0])
for d in output[1:]:
    result += ',' + str(d)     

print(result)
