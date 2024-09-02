# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

from typing import Optional


class Solution:
    def mergeTwoLists(self, list1, list2):
        list1.extend(list2)
        return sorted(list1)



sol = Solution()
print(sol.mergeTwoLists( list1 = [1,2,4], list2 = [1,3,4]))
print(sol.mergeTwoLists(list1 = [], list2 = []))
print(sol.mergeTwoLists(list1 = [], list2 = [0]))
# print(sol.mergeTwoLists())
# print(sol.mergeTwoLists())