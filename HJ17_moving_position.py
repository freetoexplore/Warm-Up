import re

input_pos = list(input('Please enter position list: ').split(';'))
init_pos = [0, 0]

for i in input_pos:
    
    if re.match('\w{1}\d{2}$', i):
        direction = i[0]
        steps = int(i[1:])
        
        if direction == 'A':
            init_pos[0] -= steps
        
        if direction == 'D':
            init_pos[0] += steps
            
        
        if direction == 'W':
            init_pos[1] += steps
        
        if direction == 'S':
            init_pos[1] -= steps
        
    else:
        init_pos[0] = init_pos[0]
        init_pos[1] = init_pos[1]

print(str(init_pos[0]) + ',' + str(init_pos[1]))