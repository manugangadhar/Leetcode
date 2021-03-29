# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        new_list1 = ListNode(0)
        new_list = new_list1
        while 1:
            if l1 is None:
                new_list.next = l2
                break
            if l2 is None:
                new_list.next = l1
                break
            if l1.val <= l2.val:
                new_list.next = l1
                l1 = l1.next
                new_list = new_list.next
            else:
                new_list.next = l2
                l2 = l2.next
                new_list = new_list.next
        return new_list1.next




