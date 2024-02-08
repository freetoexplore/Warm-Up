nums1 = [1, 2, 3, 0, 0, 0]
m = 3
nums2 = [2, 5, 6]
n = 3

nums1 = [i for i in nums1 if i != 0]
nums2 = [i for i in nums2 if i != 0]
nums = []
for i in nums1:
    nums.append(i)

for i in nums2:
    nums.append(i)
final = sorted(nums)
print(final)
