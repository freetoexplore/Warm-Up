astring = 'onetwothreefourdoublezero'
adict = {'one': 'Yi', 'two': 'Er', 'thr': 'San', 'fou': 'Si', 'fiv': 'Wu',
         'six': 'Liu', 'sev': 'Qi', 'eig': 'Ba', 'nin': 'Jiu', 'zer': 'Ling', 'dou': 1}
bdict = {'one': 3, 'two': 3, 'thr': 5, 'fou': 4, 'fiv': 4,
         'six': 4, 'sev': 5, 'eig': 5, 'nin': 4, 'zer': 4, 'dou': 6}

apart = []
res = astring
result = ''

for i in range (len(astring)):
    while res != '':
        apart.append(adict[res[:3]])
        res = res[bdict[res[:3]]:]
        
ix = 0
for i in apart:
    if i == 1:
        apart[apart.index(1)] = apart[apart.index(1) + 1]
    ix += 1
print(apart)
        
for i in apart:
    result+=i
print(result)