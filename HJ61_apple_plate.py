m_apple = 7
n_plate = 3

turns = 1
multiplier = m_apple
plates = n_plate

# ??? remove variable: turns by other length variable
for i1 in range(m_apple):
    if plates > 0:
        turns *= multiplier
        multiplier -= 1
        plates -= 1
    
# print(turns)

all_combos = []
while turns > 1:
    
    m = m_apple
    n = n_plate
    
#########################################################################                
# non-repeatable set
    
    for ini_start in range(abs(m-n)):
        combo_set = []
            
        for start_n in range(ini_start, m):
            # print('# start_n', start_n)
            if len(combo_set) < n - 1:
                # print('consider item:', start_n)
                combo_set.append(start_n)
            
            elif len(combo_set) == n - 1:
                dedup_remainder = m
                for i2 in combo_set:
                    dedup_remainder -= i2
                if dedup_remainder >= 0:
                    combo_set.append(dedup_remainder)
                
        # print(combo_set)            
        if combo_set not in all_combos and len(combo_set) == n_plate:
            all_combos.append(combo_set)
        
#########################################################################        
# repeatable sets
    
    for i3 in range(abs(m_apple - n_plate)):
        dup_set = []
        for cnt in range(n_plate):
            
            if len(dup_set) < n_plate - 1:
                dup_set.append(i3)
                
            elif len(dup_set) < n_plate:
                remainder = m_apple
                for i4 in dup_set:
                    remainder -= i4
                if remainder >= 0:    
                    dup_set.append(remainder)
     
        if dup_set not in all_combos and len(dup_set) == 3:
            all_combos.append(dup_set)
        
#########################################################################        
# dedup sets        
    all_combos_dedup = []
    for combo in all_combos:
        if combo not in all_combos_dedup:
            all_combos_dedup.append(combo) 
                        
    turns -= 1
    
print('combos', len(all_combos_dedup))
