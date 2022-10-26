binary_dict = {0: '000', 1: '001', 2: '010', 3: '011'}
b_win = []
window = '000'

input_num = 0
append_idx = len(window) - 1
test_rep_num = 0

  ### binary 3 = binary 1 + binary 2
    #   001  # binary 1
    # + 010  # binary 2
    # _____
    #   011  # binary 3

while input_num > 0 and append_idx >= 0:
    
    if test_rep_num == 2:
        window = window[: window.index('1')] + window[window.index('1'): ].replace('0', '1')
        break
    
    # add 1 if position = 0
    elif window[append_idx] == '0':
        window = window[: append_idx] + '1' + window[append_idx: -1]
        
    elif window[append_idx] == '1':
        append_idx = len(window) - 1
        window = window[: append_idx - 1] + '1' + window[append_idx - 1: ]
        
    input_num -= 1
    append_idx -= 1
    test_rep_num += 1
    
print(input_num, window)
    
