input_pairs = int(input('Enter pair nums:'))

value_dict = {}

for pair in range(input_pairs):
    input_pair = str(input('Enter pair:')).split(' ')
    
    input_idx = int(input_pair[0])
    input_val = int(input_pair[1])
    
    if input_idx in value_dict.keys():
        value_dict[input_idx] = value_dict[input_idx] + input_val
    
    else:
        value_dict[input_idx] = input_val
    
sort_dict = {}
idx_list = []

for keys in value_dict.keys():
    idx_list.append(keys)

idx_sorted = sorted(idx_list)
    
for idx in idx_sorted:
    if idx not in sort_dict.keys():
        sort_dict[idx] = value_dict[idx]

for pair in sort_dict.items():
    print(str(pair).replace('(', '').replace(')', '').split(',')[0] + str(pair).replace('(', '').replace(')', '').split(',')[1])