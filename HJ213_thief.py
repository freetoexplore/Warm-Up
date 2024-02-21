nums = [1,2,3,1]
nums = [2, 3, 2]

suma = []
sumix = []
ix = 0
for i in nums:
    
    if len(nums) == 3:
        if len(suma) == 0:
            suma.append(nums[1])
    
    elif ix -1 not in sumix and ix +1 not in sumix:
        sumix.append(ix)
        suma.append(i)    
    
    ix += 1
    
print(sum(suma))