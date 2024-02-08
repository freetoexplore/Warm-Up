# nums = [7,6,4,3,1]
nums = [7,1,5,3,6,4]
buy = min(nums)
sell = max(nums[nums.index(buy):])
print(sell-buy)
