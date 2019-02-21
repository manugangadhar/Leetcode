class Solution:

    def twoSum(self, nums, target):
        self.nums = nums
        self.target = target
        d = {}
        for i, j in enumerate(nums):
            d.update({j: i})
        for k in range(len(nums)):
            compliment = target - nums[k]
            if compliment in d.keys() and d[compliment] != k:
                return(k, d[compliment])
