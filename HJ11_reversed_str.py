asc_str = [i for i in str(input())]

idx = len(asc_str) - 1
desc_str = ''

for ix in range(0, idx + 1):
    if idx >= 0:
        desc_str = desc_str + asc_str[idx]
        idx -= 1
    
print(desc_str)