input_str = str(input())
chuck_size =  8
idx = 1

if len(input_str) <= chuck_size:
    print(input_str + '0' * (chuck_size - len(input_str)) )

elif len(input_str) % 8 == 0:
    for i in range(len(input_str) // 8):

        start_idx = idx * i * 8
        end_idx = start_idx + 8

        print(input_str[start_idx: end_idx])
        
elif len(input_str) > chuck_size and len(input_str) % 8 != 0:
    for i in range(len(input_str) // 8):

        start_idx = idx * i * 8
        end_idx = start_idx + 8

        print(input_str[start_idx: end_idx])
    
    rest_start_idx = end_idx
    rest_end_idx = len(input_str)
    rep_0 = 8 - (rest_end_idx - rest_start_idx)

    print(input_str[rest_start_idx: rest_end_idx] + '0' * rep_0)