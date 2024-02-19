str1 = '-42'
str1 = '4193 in words'
str1 = '42'
n = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
res = ''
neg = 1
for s in str1:
    if s == '-' and str1[str1.index(s) +1] in n:
        # print(neg)
        neg = -1
    if s in n:
        res = res + s
        
print(int(res)*neg)
