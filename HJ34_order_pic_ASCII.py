input_str = str(input())  # 'Ihave1nose2hands10fingers'
input_str = [input_str[ix] for ix in range(len(input_str))]
num_orders = '0123456789'
upper_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
lower_letters = 'abcdefghijklmnopqrstuvwxyz'
str_orders = num_orders + upper_letters + lower_letters

letter_cnt = {}
for l in input_str:
    keys = str(letter_cnt.keys()).replace('dict_items([', '').replace('])', '').split(',')
    
    if l in keys:
        letter_cnt[l] = letter_cnt[l] + 1
    
    else:
        letter_cnt[l] = 1

letter_order = {}
retrieve_ix = []
for l in input_str:
    vals = str(letter_order.keys()).replace('dict_items([', '').replace('])', '').split(',')

    if l not in vals:
        letter_order[str_orders.index(l)] =  l 
        retrieve_ix.append(str_orders.index(l))

retrieve_ix = sorted(retrieve_ix, reverse = False)        

# print(letter_cnt, retrieve_ix, letter_order)
res = ''
for k in retrieve_ix:
    l = letter_order[k]
    for n in range(letter_cnt[l]):
        res = res + l

print(res)