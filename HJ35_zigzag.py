input_n = int(input())

init_i = 1

# y-axis
for i in range(1, input_n +1):
    init_i = init_i + (i - 1)
    line = [init_i]
    init = init_i
    line_str = ''
    
    # x-axis
    for increment in range(i+1, input_n+1):
        init = init + increment
        line.append(init)
    
    for i in line:
        line_str = line_str + ' ' + str(i)
    print(line_str.strip())