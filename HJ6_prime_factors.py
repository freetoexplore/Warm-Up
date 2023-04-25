# 180
# 64577
# 2000000014
input_int = int(input('Input: '))

prime_flag = ''
factors = []

for factor in range(1, input_int+1):
    prime_factors = []
    if input_int%factor == 0:
        
# select prime factor
        for pf in range(1, factor + 1):
            if factor%pf == 0:
                
                prime_factors.append(pf)
                prime_factors = [i for i in set(prime_factors)]
                
        if len(prime_factors) == 2:
            
            factors.append(factor)
            
final_factors = []            
for final_factor in factors:
    if input_int%final_factor == 0:
        final_factors.append(final_factor)
        input_int = input_int/final_factor
           
res_str = ''

for num in final_factors:
    res_str = res_str + ' ' + str(num) 
    final_factors = []
    
    for factor in primes_factors:
        while input_int % factor == 0:
            
            input_int = input_int/factor
            final_factors.append(factor)
            
    res_str = ''
    
    for i in final_factors:
        res_str = (res_str + ' ' + str(i))
    
    print(res_str.lstrip())
