# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:

    def addTwoNumbers(self, l1, l2):
        l1_list = list()
        l2_list = list()
        l3 = ListNode(0)
        node = l3

        while l1:
            l1_list.append(str(l1.val))
            l1 = l1.next

        while l2:
            l2_list.append(str(l2.val))
            l2 = l2.next

        l1_list.reverse()
        l2_list.reverse()
        x1 = ''.join(l1_list)
        x2 = ''.join(l2_list)
        x3 = str(int(x1) + int(x2))
        node.val = int(x3[-1])
        for i in x3[-2::-1]:
            temp = ListNode(int(i))
            node.next = temp
            node = node.next
        return l3