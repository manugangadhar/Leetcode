def searchInsert(nums, target):
    if target in nums:
        return nums.index(target)
    else:
        for i in range(0, len(nums)):
            if target < nums[i]:
                return i
            if i == len(nums) - 1:
                return i + 1
            if nums[i] < target < nums[i + 1]:
                return i + 1


print(searchInsert([0,2,4,7,8], 2))