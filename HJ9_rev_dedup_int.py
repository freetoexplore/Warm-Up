input_int = int(input('Enter a number:'))
input_str = str(input_int)
idx_list = []

for i in range(len(input_str)):
    idx_list.append(i)
    
rev_idx = sorted(idx_list, reverse = True)

rev_num = []
for d in rev_idx:
    if input_str[d] not in rev_num:
        rev_num.append(input_str[d])
   
result = ''
for letter in rev_num:
    result = result + letter
    
print(result)