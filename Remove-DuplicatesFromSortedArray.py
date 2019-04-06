class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 0
        y = nums.copy()
        temp = []
        while i < len(y):
            if y[i] not in temp:
                temp.append(y[i])
            else:
                nums.remove(y[i])
            i = i + 1
        return len(nums)