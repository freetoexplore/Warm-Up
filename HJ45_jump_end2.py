nums = [2,3,1,1,4]
nums = [2,3,0,1,4]

s = 0
j = 0
while s <= len(nums) and j < nums[-1]:
    j = nums[j+1]    
    s += 1
    
print(s)