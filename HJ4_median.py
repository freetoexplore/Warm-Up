a = [1, 2]
b = [3]
alll = [i for i in a] + [k for k in b]

if len(alll)%2 ==0:
    median = (sorted(alll)[len(alll)//2-1] + sorted(alll)[len(alll)//2 ])/2
else:
    median = sorted(alll)[len(alll)//2 ]
    
print(median)