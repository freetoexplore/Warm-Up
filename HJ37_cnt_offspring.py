n_month = 10 # int(input())
n = n_month 
cnt = 0 

while n >= 0:
    
    for i in range(1, n): # OG
        if i > 2:
            for sib in range(2, i): # big brothers
                
                cnt += 1
        else:
            cnt -= (i-2)
            
    if n >= 3:    
        n -= 2 # pending month
    else:
        n -= 1 # ending pose
    
print(cnt)