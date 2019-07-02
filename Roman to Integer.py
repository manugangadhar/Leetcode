class Solution:
    def romanToInt(self, s: str) -> int:
        x = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        y = {'IV': 4, 'IX': 9, 'XL': 40, 'XC': 90, 'CD': 400, 'CM': 900}

        i = 0
        intnum = 0

        if len(s) == 1:
            return x[s[i]]
        else:
            while i < len(s) - 1:
                if s[i] + s[i + 1] in y:
                    intnum = intnum + y[s[i] + s[i + 1]]
                    i = i + 2
                else:
                    intnum = intnum + x[s[i]]
                    i = i + 1
                if i == len(s) - 1:
                    intnum = intnum + x[s[i]]
            return intnum