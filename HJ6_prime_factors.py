## Ex. find all prime factors in an input number     
# list all prime numbers < input number
input_num = int(input()) # 2*10**9+14+1

prime_in_range = []
for num in range(1, input_num + 1):
    n_factor = []
    for factor in range(1, num + 1):
        if num%factor == 0:
            n_factor.append(factor)
    if len(n_factor) == 2:
        prime_in_range.append(factor)

# divide input number by prime numbers in list
prime_divisor = []
for prime in prime_in_range:
    if input_num%prime == 0:
        prime_divisor.append(prime)
        

# dvide by prime factors
prime_list = ''
for p in prime_divisor:
    while input_num%p == 0:
        prime_list += ' ' + str(p)
        input_num = input_num/p

print(prime_list.lstrip())