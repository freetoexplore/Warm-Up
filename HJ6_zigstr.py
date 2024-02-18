s = "PAYPALISHIRING"
s = 'A'
numRows = 3
numRows  = 1
res = [s[0]]

ix = 0
while ix < len(s) - (4 + 2):
    ix_next = ix + numRows + 1
    res.append(s[ix_next])
    ix += 4 + 2
    
n = -1    
while numRows != 1 and n < len(s) - 1:
    n_next = n + 2
    res.append(s[n_next])
    n += 2
    
idx = -2
while numRows != 1 and idx < len(s) - (4+2):
    ix_next = idx + numRows + 1
    res.append(s[ix_next])
    idx += 4 + 2

result = ''
for k in res:
    result = result +k    
print(result)