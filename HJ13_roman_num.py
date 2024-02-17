d = {'I': 1, 'IV': 4, 'V': 5, 'IX': 9, 'X': 10, 'XL': 40, 'L': 50, 'XC': 90,  'C': 100, 'CD': 400, 'D': 500, 'CM': 900, 'M': 1000}
s = 'MCMXCIV'
s = 'IV'
s = 'IX'
s ='LVIII'
res = 0
ix = 0
while ix < len(s):
    str1 = s[ix:ix + 2]
    if str1 in d.keys():
        res += d[str1]
        ix += 2
    else:
        res += d[s[ix]]
        ix += 1
        
print(res)