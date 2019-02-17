class Solution:
    def threeSum(self, nums: 'List[int]') -> 'List[List[int]]':

        s = sorted(nums)
        output = []
        for k in range(len(s)):
            target = -s[k]
            i, j = k + 1, len(s) - 1
            while i < j:
                sum_two = s[i] + s[j]
                if sum_two < target:
                    i += 1
                elif sum_two > target:
                    j -= 1
                else:
                    temp = [s[k], s[i], s[j]]
                    temp.sort()
                    if temp not in output:
                        output.append(temp)
                    i += 1
                    j -= 1
        return output