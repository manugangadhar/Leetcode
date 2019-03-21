def letterCombinations(digits):
    numbers_dict = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', '6': 'mno', '7': 'pqrs', '8': 'tuv',
                    '9': 'wxyz'}
    output = []
    index_dict = {}
    if len(digits) == 0:
        return output
    elif len(digits) == 1:
        return list(numbers_dict[digits])
    else:
        for i, j in enumerate(digits):
            index_dict[i] = 0
        count_fromlast = len(digits) - 2

        while index_dict[0] < len(numbers_dict[digits[0]]):
            temp = ''
            i = 0
            while i < len(digits):
                if i == len(digits) - 1:
                    count_numberlength = 0
                    while count_numberlength < len(numbers_dict[digits[len(digits) - 1]]):
                        output.append(temp + numbers_dict[digits[len(digits) - 1]][count_numberlength])
                        count_numberlength = count_numberlength + 1
                    print(output)
                    print(index_dict)
                    print(count_fromlast)
                    if index_dict[count_fromlast] < len(numbers_dict[digits[count_fromlast]]) - 1:
                        index_dict[count_fromlast] = index_dict[count_fromlast] + 1
                        temp = ''
                        i = 0
                        continue
                    else:
                        if count_fromlast == 0:
                            index_dict[count_fromlast] = index_dict[count_fromlast] + 1
                            break
                        else:
                            index_dict[count_fromlast] = 0
                            for p in range(count_fromlast - 1, -1, -1):
                                if p == 0:
                                    index_dict[p] = index_dict[p] + 1
                                    break
                                else:
                                    if index_dict[p] >= len(numbers_dict[digits[p]]) - 1:
                                        index_dict[p] = 0
                                    else:
                                        index_dict[p] = index_dict[p] + 1
                                        break
                            count_fromlast = len(digits) - 2
                            break
                else:
                    temp = temp + numbers_dict[digits[i]][index_dict[i]]
                i = i + 1
        return output


print(letterCombinations("5678"))
