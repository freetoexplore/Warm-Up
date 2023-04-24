# 180
# 64577
# 2000000014
input_int = int(input('Input: '))

prime_flag = ''
factors = []

for factor in range(1, input_int+1):
    if input_int%factor == 0:
        factors.append(factor)
        
# prime number
if len(factors) == 2:
    prime_flag == 'Y'
    print(input_int)
        
# not prime number
else:
    prime_flag = 'N'
    
    primes_factors = []
    nums = [i for i in factors]

    for num in nums:
        factors = []
        for factor in range(2, num + 1):
            
            if num % factor == 0:
                factors.append(factor)
             
        if len(factors) == 1:
            primes_factors.append(num) 
            
    # print(primes_factors)    
    final_factors = []
    
    for factor in primes_factors:
        while input_int % factor == 0:
            
            input_int = input_int/factor
            final_factors.append(factor)
            
    res_str = ''
    
    for i in final_factors:
        res_str = (res_str + ' ' + str(i))
    
    print(res_str.lstrip())
