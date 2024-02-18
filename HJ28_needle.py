haystack = "sadbutsad"
needle = "sad"
window = len(needle)
res = -1
for i in range(len(haystack) - window):
    if haystack[i:i+window] == needle:
        res = i
        break
    
print(res)