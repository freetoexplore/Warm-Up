class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        add_i = 0

        for i in range(len(nums)):
            init_num = nums[i]

            for num in nums[i+1:]:
                if init_num != num and init_num + num == target:
                    return (i, nums.index(num))

                if init_num == num and init_num + num == target:
                    del nums[i]
                    add_i += 1
                    return (i, nums.index(num)+add_i)