class Solution:
    def lengthOfLongestSubstring(self, s: 'str') -> 'int':
        result_len = []
        temp = ''
        i = 0
        j = i
        if len(s):
            while i < len(s):
                if j < len(s) and s[j] not in temp:
                    temp = temp + s[j]
                    j = j + 1
                else:
                    result_len.append(len(temp))
                    temp = ''
                    i = i + 1
                    j = i
            return(max(result_len))
        else:
            return 0