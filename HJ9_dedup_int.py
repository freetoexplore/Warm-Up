input_num = int(input())
input_str = str(input_num)

i = len(input_str) - 1
output = ''
now_str = ''

while i >= 0:
    if input_str[i] not in now_str:
        output = output + input_str[i]
        
        now_str = now_str + input_str[i]    
    i -= 1
        
print(now_str)