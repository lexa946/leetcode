# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:


        index = 1
        recv = head[0]
        while True:
            if len(head) == index:
                break
            if recv == head[index]:
                recv = head.pop(index)
                index += 1

        return head








sol = Solution()
print(sol.deleteDuplicates(head = [1,1,2]))
