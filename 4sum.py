nums = [-5,-3,2,-1,0,7,-2,-3,-10,-3,-4,7,-5,0,-7,10,5,6,-6]
target = 2
new_list1 = []
new_list2 = []
result_list = []
count = 0
print(nums)
if len(nums) > 4:
    for i in range(0, len(nums)):
        list1 = nums.copy()
        list1.pop(i)
        for j in range(0, len(list1)):
            new_list1.append(nums[i])
            if j+3 <= len(list1):
                new_list1.extend(list1[j:j+3])
                new_list2.extend(list1[0:j])
                new_list2.extend(list1[j+3:])
            else:
                new_list1.extend(list1[j:])
                new_list2.extend(list1[4 - len(new_list1):j])
                new_list1.extend(list1[0: 4 - len(new_list1)])
            for k in range(0, len(new_list1)):
                for l in range(0, len(new_list2)):
                    temp_list1 = new_list1.copy()
                    temp_list1[k] = new_list2[l]
                    temp_list1_sorted = temp_list1.copy()
                    temp_list1_sorted.sort()
                    if temp_list1_sorted not in result_list and sum(temp_list1_sorted) == target:
                        result_list.append(temp_list1_sorted)
                    temp_list1_sorted = []
                    temp_list2 = new_list2.copy()
                    temp_list2.pop(l)
                    temp_list2.append(new_list1[k])
                    if new_list1 == temp_list1 and new_list2 == temp_list2:
                        temp_list1 = []
                        temp_list2 = []
                    else:
                        for m in range(0, len(temp_list1)):
                            for n in range(0, len(temp_list2)):
                                temp_list3 = temp_list1.copy()
                                temp_list3[m] = temp_list2[n]
                                temp_list3.sort()
                                if temp_list3 not in result_list and sum(temp_list3) == target:
                                    result_list.append(temp_list3)
                                temp_list3 = []
                        temp_list1 = []
                        temp_list2 = []
            new_list1 = []
            new_list2 = []
    print(result_list)
    print(len(result_list))
elif len(nums) == 4:
    if sum(nums) == target:
        print([nums])
    else:
        print(result_list)
else:
    print(result_list)
