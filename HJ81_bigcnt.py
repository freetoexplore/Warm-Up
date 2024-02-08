# nums = [3, 2, 3]
nums = [2,2,1,1,1,2,2]
cnts = {}
result = []
for i in nums:
    if i not in cnts.keys():
        cnts[i] = 1
    else:
        cnts[i] += 1
        
for pair in cnts.items():
    if pair[1] > len(nums)/2:
        result.append(pair[0])

for r in result:        
    print(r)
