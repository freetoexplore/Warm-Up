citations = [1, 3, 1]
# citations = [3,0,6,1,5]
n = []
h = 0
for c in citations:
    if c > 0:
        n.append(c)
        h += 1
        
min_n = min(n)
len_n = len(n)

if min_n < len_n:
    n = [i for i in n if i != min(n)]
h = len(n)    
print(h)
