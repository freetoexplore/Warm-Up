n_lines = int(input())
init_line = [1]
all_lines = [init_line]
turns = 1

if n_lines == 0:
    line = [0]
    print()
        
elif n_lines == 1:
    print(-1)

else:        

    # each line
    while turns < n_lines:
        aline = []
        line_len = 0

        # each number
        for ix in range(0, 2*turns + 1):
            sum_cnt = 0
            sums = []
            num_sum = 0
            
            if ix - 2 >= 0 and ix - 2 < len(init_line):
                sum_cnt += 1
                sums.append(init_line[ix- 2])
                # print('Yes 1', '*ix', ix, '*ix- 2', ix- 2)
                
            if ix - 1 >= 0 and ix - 1< len(init_line):
                sum_cnt += 1
                sums.append(init_line[ix- 1])
                # print('Yes 2','*ix', ix, '*ix- 1', ix- 1)
                
            if ix >= 0 and ix < len(init_line):
                # print('Yes 3')

                # print('sums', sums, 'ix', ix, 'init_line', init_line)

                sum_cnt += 1
                sums.append(init_line[ix])

                
            if sum_cnt >= 1:
                # print('sums', sums)
                aline.append(sum(sums))
                line_len += 1
                # print(aline, 'aline')
                        
        # print(aline, 'aline')
        all_lines.append(aline)

        turns += 1
        init_line = aline    
        
    res_line = all_lines[n_lines - 1] 
    result = -1
    res_cnt = 1
    for n in res_line:
        if n%2 != 0:
            res_cnt +=1
        else:    
            break
    
    if res_cnt != 1 and res_cnt < len(res_line) - 1:
        print(res_cnt)
            
    else:
        print(result)
        
def print_plot():
    n_indent = 0
    cnt = 0
    for line in all_lines:
        
        sps= ''
        spc = line_len//2*2
        spc_r = line_len%2
        for s in range(spc - n_indent):
            sps += ' '
            
        res_line = ''
        for _ in range(line_len):
            if _ in [ix for ix in range(len(line))]:
                res_line = res_line + str(line[_]) + ' '
                
            else:
                res_line = res_line + ' '
                
        if cnt >= 0:
            n_indent += 2
    
        cnt += 1
        print(sps, res_line)

# print_plot()