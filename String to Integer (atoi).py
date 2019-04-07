class Solution:
    def myAtoi(self, str: str) -> int:
        result = []
        many_plusminus = 0
        whitespace_begin = 1
        i = 0
        if len(str) == 1 and str[i].isdigit():
            result.append(str[i])
        elif len(str) == 1 and not (str[i].isdigit()):
            result = []
        else:
            while i < len(str):
                if str[i].isspace():
                    if i == 0:
                        j = i + 1
                        while j < len(str) and str[j].isspace():
                            j = j + 1
                        i = j
                    else:
                        result = []
                        break
                elif str[i].isdigit():
                    result.append(str[i])
                    j = i + 1
                    while j < len(str) and str[j].isdigit():
                        result.append(str[j])
                        j = j + 1
                    break
                elif str[i] == '+' or str[i] == '-':
                    if '+' in result or '-' in result:
                        result = []
                        break
                    else:
                        result.append(str[i])
                    i = i + 1
                else:
                    result = []
                    break
        if result == []:
            return 0
        else:
            if -(2 ** 31) <= int(''.join(result)) <= ((2 ** 31) - 1):
                return int(''.join(result))
            else:
                if int(''.join(result)) < -(2 ** 31):
                    return -(2 ** 31)
                else:
                    return (2 ** 31) - 1

