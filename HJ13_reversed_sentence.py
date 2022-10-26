# reversed sentence
asc_str = [i for i in str(input('Please enter a sentence: ')).split(' ')]
asc_str

idx = len(asc_str) - 1
desc_str = ''

for ix in range(0, idx + 1):
    if idx >= 0:
        desc_str = desc_str + ' ' + asc_str[idx]
        idx -= 1
    
print((desc_str).lstrip())