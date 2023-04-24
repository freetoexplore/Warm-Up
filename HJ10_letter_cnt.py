# for loop save letters in string by list. 
# split() truncate by unit in 'word'

input_str = str(input())
cnt = 0
letter_list = []

for i in input_str:
    if i not in letter_list:
        cnt += 1
        letter_list.append(i)

print(cnt)