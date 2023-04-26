input_str = str(input('Input charge and amount:'))
total_charge = int(input_str.split(' ')[0])
total_amount = int(input_str.split(' ')[1])

prod_prc = []
prod_wgt = []
prod_pid = []
load_prod = []
idx = 1

for terms in range(total_amount):
    item_info = input('Input items:') +' '+ str(idx)
    load_prod.append(item_info)

    prod_prc.append(int(item_info.split(' ')[0]))
    prod_wgt.append(int(item_info.split(' ')[1]))
    prod_pid.append(int(item_info.split(' ')[2]))
    
    idx += 1
    
print(prod_prc)

# compound product price with its main part
amount = 0
satisfaction_score = []

append_flag = 'N'
score = 0
last_turn = 0

for idx in range(len(prod_pid)):
    
    idx += last_turn
    last_turn = 0
    
    while idx < len(prod_pid) - 1 or append_flag == 'Y':
        print('flag 1')
        if amount <= total_amount or total_charge >= 0:
                    satisfaction_score.append(score)
                    append_flag = 'N'
                    
        else:
            append_flag = 'N'
            break
            
        for idx in range(len(prod_pid)):
            p = prod_prc[idx]
            
        # when first item is main part
            if prod_pid[idx] == 0:
                v = prod_wgt[idx]
                
                amount += 1
                total_charge -= p
                score += p*v
                
                if amount <= total_amount and total_charge >= 0:
                    satisfaction_score.append(score)
                else:
                    break
                        
        # when first item is appendix part
            else:
                if prod_pid[idx] != 0:
                    append_flag = 'Y'
                    last_turn = 1
                    
            # score & charge on appendix part
                v_append = prod_wgt[idx]
                
                amount += 1
                total_charge -= p
                score += p*v_append
                
            # score & charge on its main part
                id_main = prod_pid[idx]
                p_main = prod_prc[id_main - 1]
                v_main = prod_wgt[id_main - 1]
                
                amount += 1
                total_charge -= p
                score += p_main*v_main
                print('flag 2')
                
        print('iteration score:', satisfaction_score, idx, total_amount, total_charge, append_flag)
    
result = max(satisfaction_score)
print('best score', result)