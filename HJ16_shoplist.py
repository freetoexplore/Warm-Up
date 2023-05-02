### NOT FINAL VERSION !!! ###
import math
input0 = str(input())
budget = int(input0.split(' ')[0])
n_constraint = int(input0.split(' ')[1])

def extract_num(input_str, place):
    return int(input_str.split(' ')[place])

prices = []
values = []
main_id = []

for i in range(int(input0.split(' ')[1])):
    intake_str = str(input())
    prices += [extract_num(intake_str, 0) ]
    values += [extract_num(intake_str, 1) ]
    main_id +=[extract_num(intake_str, 2) ]

main_id_clean = []

### start to script
for i in main_id: 
    if i != 0:
        main_id_clean.append(i)
    else:
        main_id_clean.append(math.nan)
        
budget = int(input0.split(' ')[0])
n_constraint = int(input0.split(' ')[1])
scores_list = []


round_turns = 0
max_turns = n_constraint
step_range_init = [i for i in range(n_constraint)]

while round_turns < max_turns:
    scores = 0
    # print('round {0}'.format(round_turns))
    step_range = step_range_init[round_turns:] + step_range_init[:round_turns]
    # print(step_range)
    
    step_list = []
    
    for step in step_range:
        step_list.append(step)
        
    # main part    
        if main_id[step] == 0:
            p = prices[step]
            v = values[step]
            budget -= p
            n_constraint -= 1
            scores += p*v
            
            if budget >= 0 and n_constraint >= 0:
                scores_list.append(scores)
            
    # appendix part        
        else:
            p_appendix = prices[step]
            v_appendix = values[step]
            
            budget -= p_appendix
            n_constraint -= 1
            scores += p_appendix*v_appendix
            
            step_main = main_id[step] - 1
            p_main = prices[step_main]
            v_main = values[step_main]
            
            if step_main not in step_list:
                budget -= p_main
                n_constraint -= 1
                scores += p_main*v_main
            
            if budget >= 0 and n_constraint >= 0:
                scores_list.append(scores)
     
    round_turns += 1
    n_constraint = int(input0.split(' ')[1])
    budget = int(input0.split(' ')[0])
    
print(max(scores_list))
