class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        i = abs(divisor) ** 13
        j = 0
        if abs(divisor) == 1:
            j = abs(dividend)
        else:
            while True:
                if i <= abs(abs(dividend) - (abs(divisor)**13)):
                    j = j + abs(divisor) ** 12
                    i = i + (abs(divisor) ** 13)
                else:
                    if i == abs(divisor) ** 13:
                        i = abs(divisor)
                    elif abs(abs(dividend) - (abs(divisor) ** 13)) <= i <= abs(dividend):
                        i = i - (abs(divisor) ** 13)
                        j = j - 1
                    while i <= abs(dividend):
                        i = i + abs(divisor)
                        j = j + 1
                    break

        if (divisor < 0) and (dividend < 0):
            if j >= 2**31:
                return (2**31 - 1)
            else:
                return j
        elif (divisor < 0) or (dividend < 0):
            if j < -(2**31):
                return -(2**31)
            else:
                return int('-' + str(j))
        else:
            if j >= 2**31:
                return (2**31 - 1)
            else:
                return j


