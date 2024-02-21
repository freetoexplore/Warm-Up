head = [1,2,3,4,5]
head = [1,2]
n = len(head) - 1
res = []
while n >= 0:
    res.append(head[n])
    n -= 1
    
print(res)