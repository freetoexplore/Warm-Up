input_str = str(input())

str_idx = []

for idx in range(len(input_str)):
    str_idx.append(idx)


rev_str_idx = sorted(str_idx, reverse = True)

result_str = ''

for idx in rev_str_idx:
    result_str = result_str + input_str[idx]

print(result_str)