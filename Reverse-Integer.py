class Solution:
    def reverse(self, x: int) -> int:
        if x < 0:
            x_str = str(x)[1:]
            if int('-' + x_str[::-1]) >= -2 ** 31:
                return int('-' + x_str[::-1])
            else:
                return 0
        else:
            x_str = str(x)
            if int(x_str[::-1]) <= (2 ** 31) - 1:
                return int(x_str[::-1])
            else:
                return 0