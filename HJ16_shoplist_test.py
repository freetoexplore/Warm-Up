import math
input0 = '2000 10'# '1000 5'# '50 5' # '1500 7'#  
input1 = '500 1 0'# '800 2 0'# '20 3 5' # '500 3 5' #  
input2 = '400 4 0'# '400 5 1'# '20 3 5' # '400 4 0' # 
input3 = '300 5 1'# '200 5 1' # '10 3 0' # '300 5 1' # 
input4 = '400 5 1'# '400 3 0'# '10 2 0'# '400 5 1' # 
input5 = '200 5 0' # '500 2 0'# '10 1 0'# '200 5 0' # 
input6 = '500 4 5' # '500 4 0'
input7 = '400 4 0' # '400 4 0'
input8 = '320 2 0' # '400 4 0'
input9 = '410 3 0'
input10 = '400 3 5'

def extract_num(input_str, place):
    return int(input_str.split(' ')[place])

prices = [extract_num(input1, 0), extract_num(input2, 0), extract_num(input3, 0), extract_num(input4, 0), extract_num(input5, 0)
           , extract_num(input6, 0), extract_num(input7, 0),  extract_num(input8, 1)
           , extract_num(input9, 2), extract_num(input10, 2)
          ]
values = [extract_num(input1, 1), extract_num(input2, 1), extract_num(input3, 1), extract_num(input4, 1), extract_num(input5, 1)
           , extract_num(input6, 1), extract_num(input7, 1),  extract_num(input8, 1)  
           , extract_num(input9, 2), extract_num(input10, 2)
          ]
main_id = [extract_num(input1, 2), extract_num(input2, 2), extract_num(input3, 2), extract_num(input4, 2), extract_num(input5, 2)
             , extract_num(input6, 2), extract_num(input7, 2),  extract_num(input8, 2)
             , extract_num(input9, 2), extract_num(input10, 2)
            ]


########################### input ##############################


# import math
# input0 = str(input())
# budget = int(input0.split(' ')[0])
# n_constraint = int(input0.split(' ')[1])

# def extract_num(input_str, place):
#     return int(input_str.split(' ')[place])

# prices = []
# values = []
# main_id = []

# for i in range(int(input0.split(' ')[1])):
#     intake_str = str(input())
#     prices += [extract_num(intake_str, 0) ]
#     values += [extract_num(intake_str, 1) ]
#     main_id +=[extract_num(intake_str, 2) ]


########################### start script ##############################
main_id_clean = []
for i in main_id: 
    if i != 0:
        main_id_clean.append(i)
    else:
        main_id_clean.append(math.nan)
        

budget = int(input0.split(' ')[0])
n_constraint = int(input0.split(' ')[1])
scores_list = []
# scores = 0

round_turns = 0
max_turns = n_constraint
step_range_init = [i for i in range(n_constraint)]

while round_turns < max_turns:
    scores = 0
    # n_constraint = max_turns
    budget = int(input0.split(' ')[0])
    print('----------------------{0} turn start----------------------'.format(round_turns))
    # print('round {0}'.format(round_turns))
    step_range = step_range_init[round_turns:] + step_range_init[:round_turns]
    print('step range', step_range)
    main_prod_list = []

    step_list = []
    for step in step_range:
        
    # main part    
        if main_id[step] == 0:
            step_list.append(main_id[step])
            main_prod_list.append(step)
            p = prices[step]
            v = values[step]
            
            budget -= p
            n_constraint -= 1
            scores += p*v
            # print('remove price', prices, step)
            # print('main step', step, 'score', scores)
            
            if budget >= 0 and n_constraint >= 0:
                scores_list.append(scores)
            
            else:
                # no monney buy main part, return money back
                budget += p
                n_constraint += 1
                scores -= p*v
                main_prod_list = [i for i in main_prod_list if i != step] 
            #     print('step', step, 'price', p, 'score', scores)
            # print('*main   step:', step, 'round:',round_turns,'score:',scores,'budget', budget, 'amount:', n_constraint, scores_list)
            
    # appendix part  ??? loop in second append part when budget >= 0      
        else:
            
            p_appendix = prices[step]
            v_appendix = values[step]
            
            budget -= p_appendix
            n_constraint -= 1
            scores += p_appendix*v_appendix
            step_main = main_id[step] - 1
            # print('appends main part id', step_main, 'step list', step_list)
            
            pre_added = ''
            if step_main not in step_list :
                print('*** check first appendix product***')
                step_list.append(step_main)
                
                main_prod_list.append(step)
                
                p_main = prices[step_main]
                v_main = values[step_main]
                
                budget -= p_main
                n_constraint -= 1
                scores += p_main*v_main
                if step_main <= step:
                    pre_added = 'Y'
            
            if budget >= 0 and n_constraint >= 0:
                scores_list.append(scores)
                print('added apendix price', p_appendix, 'budget', budget)
                
            if budget < 0:
                
                rm_append_id = []
                if len(main_prod_list) > 0:
                    target_rm_id_main = main_prod_list[-1]
                    
                    for ix in main_id:
                        if ix == target_rm_id_main:

                            rm_append_id.append(step)
                        
                rm_append_id = [i for i in set(rm_append_id)]
                print('remove appendix id', rm_append_id)  
                    
                for rm_idx in rm_append_id:
                    p_appendix = prices[rm_idx]
                    v_appendix = values[rm_idx]
                        
                    n_constraint += 1 # appendix
                    scores -= p_appendix*v_appendix
                    budget += p_appendix
                
                    if pre_added == 'Y': # pre-added main part
                        n_constraint += 1 
                        scores -= p_main*v_main
                        budget += p_main
                
                
            # print('**append step', step, 'main step', step_main, 'round', round_turns,'score',scores, 'budget', budget, 'amount:', n_constraint, scores_list, 'main step covered:', step_list)
                
            print('round', round_turns, 'scores:', scores_list)        
    round_turns += 1
    n_constraint = int(input0.split(' ')[1])
    budget = int(input0.split(' ')[0])
    
print(max(scores_list))

