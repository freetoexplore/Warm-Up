s = "the sky is blue"
s = "a good   example"
ss = [i for i in s.split(' ') if len(i) != 0]
print(ss)
ix = 0
res = []
while ix < len(ss):
    idx = len(ss) - ix - 1
    res.append(ss[idx])
    ix += 1
    
result = ''
for i in res:
    result = result + i + ' '
    
print(result.rstrip())