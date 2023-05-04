input_str = str(input())
dict_l = {}

for letter in input_str:
    if letter not in dict_l.keys():
        dict_l[letter] = 1
    else:
        dict_l[letter] = dict_l[letter] + 1

min_cnt = min(dict_l.values())

result = ''
for l in input_str:
    key = l
    if int(dict_l[key]) != min_cnt:
        result = result + str(key)
        
print(result)
