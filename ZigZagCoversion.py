class Solution:
    def convert(self, s: 'str', numRows: 'int') -> 'str':
        gap = (2 * numRows) - 3
        i = 0
        index_result_string = []
        k = numRows + (numRows - 5)
        if len(s) == 1 or numRows == 1:
            return s
        else:
            while i < numRows:
                j = i
                while j < len(s):
                    index_result_string.append(j)
                    if i > 0 and (j + k + 1) < len(s) and i < (numRows -1):
                        index_result_string.append(j + k + 1)
                    j = (j + gap) + 1
                if i!= 0:
                    k = k - 2
                i = i + 1

            result_string = ""
            for i in index_result_string:
                result_string = result_string + s[i]
            return result_string

