class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        list3=[]
        i = 0
        j = 0
        for k in range(0, len(nums1) + len(nums2)):
            if i == len(nums1):
                merged_list = list3 + nums2[j:len(nums2)]
                if len(merged_list)%2 == 0:
                   return float((merged_list[int((len(merged_list) + 1) / 2) - 1] + merged_list[int((len(merged_list) + 2) / 2) - 1]) / 2)
                else:
                    return float(merged_list[int(len(merged_list)/2)])
                break
            if j == len(nums2):
                merged_list = list3 + nums1[i:len(nums1)]
                if len(merged_list)%2 == 0:
                    return float((merged_list[int((len(merged_list) + 1) / 2) - 1] + merged_list[int((len(merged_list) + 2) / 2) - 1]) / 2)
                else:
                    return float(merged_list[int(len(merged_list)/2)])
                break
            if nums1[i] <= nums2[j]:
                list3.insert(k, nums1[i])
                i = i + 1
            else:
                list3.insert(k, nums2[j])
                j = j + 1

