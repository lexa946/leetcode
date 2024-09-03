# Definition for singly-linked list.
from copy import copy
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        return f'{self.val}'


class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        if not head: return None
        heads_new = []

        while head:
            if head.val != val:
                heads_new.append(head)

            head = head.next

        if not heads_new: return None
        # i = len(heads_new)
        prev_head = heads_new.pop()
        prev_head.next = None
        current_head = prev_head
        while heads_new:
            current_head = heads_new.pop()
            current_head.next = prev_head
            prev_head = current_head

        return current_head


node_one = ListNode(1)
node_two = ListNode(2)
node_tree = ListNode(6)
node_four = ListNode(4)
node_five = ListNode(5)
node_six = ListNode(6)
# node_one = ListNode(7)
# node_two = ListNode(7)
# node_tree = ListNode(7)
# node_four = ListNode(7)

# node_one.next = node_two
node_two.next = node_tree
node_tree.next = node_four
node_four.next = node_five
node_five.next = node_six
# node_four.next = node_two


sol = Solution()
print(sol.removeElements(node_one, 2))
