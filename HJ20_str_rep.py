import sys
import re

df = sys.stdin.read().strip()
input_strs = [i for i in df.split("\n")]
def check_req(input_str):

    # req 1
    req1 = 'N'
    if len(input_str) <= 8:
        print('NG')
        req1 = 'Y'
        
    # req 2
    req2 = 'N'
    while req2 == 'N':
        
        typr_cnt = 0
        if re.search(r'[A-Z]', input_str) != True:
            typr_cnt +=1
    
        elif re.search(r'[a-z]', input_str) != True:
            typr_cnt +=1
    
        elif re.search(r'\d', input_str) != True:
            typr_cnt +=1
    
        elif re.search(r"[~!@#$%^&*()_+`{}|[]\:';<>?,./]", input_str) != True or re.search(r"[']", input_str) != True:
            typr_cnt +=1
    
        elif typr_cnt < 3:
            print('NG')
            req2 = 'Y'
    
        elif re.search(r"\s", input_str) == True or re.search(r"\n", input_str) == True:
            print('NG')
            req2 = 'Y'
        
        else:
            req2 == 'N'
        
        break
    
    req3 = 'N'
    while req3 == 'N':
        
        # req 3
        window_size = 3
        patterns = []
        
        # single word
        for start_ix in range(len(input_str) - window_size):
            
            pattern = str(input_str[start_ix: start_ix+3].lower())
            patterns.append(pattern)
            
        patterns_cnt = {}
        for subword in patterns:    
            if subword in patterns_cnt.keys():
                patterns_cnt[subword] = patterns_cnt[subword] + 1
                
            else:
                patterns_cnt[subword] = 1
                
        for kv_pair in patterns_cnt.items():
            v = kv_pair[1]
            if v >= 2:
                print('NG')
                req3 = 'Y'
                
        break
                            
    while req1 == 'N' and req2 == 'N' and req3 == 'N':
        print('OK')
        break

for input_str in input_strs:
    check_req(input_str)
