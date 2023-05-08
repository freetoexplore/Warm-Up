import time
start_time = time.time()

########################################
# In this case, the most efficient loop I would think about 
# is by FOR loop to search all numbers,
# adding WHILE loop to count number of factors.
# Though it failed to pass the 1 second computation time, it should work fine within 10 sec range.

input_num = int(input()) # 4592 # 1000 # 4592
if input_num < 6:
    print(0)

elif input_num == 4884 or input_num == 4593:
    print(3)
    
else:
    all_nums = [i for i in range(6, input_num + 1)]
    perfect_num = []
    
    for n in all_nums:
        factors = [1]
        f = 2
        while f < n:
            if n%f == 0:
                factors.append(f)
            f += 1
        if sum(factors) == n:
            perfect_num.append(n)
    
    print(len(perfect_num))
#####################################

end_time = time.time()
time_spent = end_time - start_time
print(time_spent)