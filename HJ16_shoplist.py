import math
input0 = '1000 5'# '50 5'# 
input1 = '800 2 5' # '20 3 5'# 
input2= '400 5 1' # '20 3 5'# 
input3 = '300 5 1' # '10 3 0'# 
input4 = '400 3 0' # '10 2 0'# 
input5 = '500 2 0' # '10 1 0'# 

def extract_num(input_str, place):
    return int(input_str.split(' ')[place])

prices = [extract_num(input1, 0), extract_num(input2, 0), extract_num(input3, 0), extract_num(input4, 0), extract_num(input5, 0)]
values = [extract_num(input1, 1), extract_num(input2, 1), extract_num(input3, 1), extract_num(input4, 1), extract_num(input5, 1)]
main_id = [extract_num(input1, 2), extract_num(input2, 2), extract_num(input3, 2), extract_num(input4, 2), extract_num(input5, 2)]
main_id_clean = []

### start to script

for i in main_id: 
    if i != 0:
        main_id_clean.append(i)
    else:
        main_id_clean.append(math.nan)
        
print(main_id_clean)

budget = int(input0.split(' ')[0])
n_constraint = int(input0.split(' ')[1])
scores_list = []


round_turns = 0
max_turns = n_constraint
step_range_init = [i for i in range(n_constraint)]

while round_turns < max_turns:
    scores = 0
    print('round {0}'.format(round_turns))
    step_range = step_range_init[round_turns:] + step_range_init[:round_turns]
    print(step_range)
    
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
            print('main   step:', step, 'round:',round_turns,'score:',scores,'budget', budget, 'amount:', n_constraint, scores_list)
            
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
                
            print('append step', step, 'main step', step_main, 'round', round_turns,'score',scores, 'budget', budget, 'amount:', n_constraint, scores_list, 'step list:')
                
    print('round', round_turns, 'scores:', scores_list)        
    round_turns += 1
    n_constraint = int(input0.split(' ')[1])
    budget = int(input0.split(' ')[0])
    
print(max(scores_list))
