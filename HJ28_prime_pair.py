# n_nums = int(input())

# n_nums = '20867 25786 13932 11112 18239 25481 2607 8855 9788 28461 27950 9814'
# n_nums = '2 5 6 13'
# n_nums = '3 6'
# n_nums = '3 8'
n_nums= '20923 22855 2817 1447 29277 19736 20227 22422 24712 27054 27050 18272 5477 27174 13880 15730 7982 11464 27483 19563 5998 16163'
input_list = [int(i) for i in (n_nums.split(' '))]

if len(input_list) == 2 and sum(input_list) % 2 == 0:
    print(0)

else:
    test =[]
    # prime limits
    max_num = max(input_list)
    # nums = [i for i in range(1, (max_num+1)*2)]
    
    # compound primes
    prime_pair = 0
    for n1 in input_list:
        if n1 in input_list:
            # print('n1', n1)
            # print('******new turn input_list*****', input_list)
            # print(input_list, n1)
            for n2 in [i for i in input_list if i != n1]:
                if n2 in input_list and n1 in input_list:
                    
                    
                    sum2 = [n1 + n2]
                    # print('sum2', sum2)
                    for num in sum2:
                        f = 1
                        n_factor = []
                    
                        while f <= num:
                            
                            if num%f == 0:
                                n_factor.append(f)
                                n_factor = [i for i in set(n_factor)]
                                # print(num, n_factor)
                            f += 1    
                            
                        if len(n_factor) == 2:
                            prime_pair += 1
                            input_list = [i for i in input_list if (i != n1) ]
                            input_list = [i for i in input_list if (i != n2) ]
                            test.append(n1)
                            test.append(n2)                            
                        
    print(prime_pair)

# test for answer: reported to system as the answer should be 7 groups rather 8.
diff = [i for i in input_list if i not in test]
print('good pairs', test, '\nrest pairs', diff)
for n1 in diff:
    for n2 in diff:
        if n2 != n1:
            # if ((n1+n2)%2 != 0) and ((n1+n2)%3 != 0 )and ((n1+n2)%5 != 0):
                print(n1,'+', n2,'=', n1+n2)    
        diff = [i for i in diff if i != n1]