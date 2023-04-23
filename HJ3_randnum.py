# input of first line
num_cnt = int(input())

input_list = []
for i in range(num_cnt):
    input_list.append(int(input()))

for num in set(input_list):
    print(num)