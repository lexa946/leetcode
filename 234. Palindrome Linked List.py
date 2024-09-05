from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if not head: return False
        vals = self.get_val(head)
        if len(vals) == 1: return True

        if len(vals) % 2 == 1:
            right = int(len(vals) / 2) + 1
            left = right - 2
            iter_count = right - 1
        else:
            right = int(len(vals) / 2)
            left = right - 1
            iter_count = right

        for i in range(iter_count):
            if vals[left] != vals[right]:
                return False
            left -= 1
            right += 1

        return True

    # def get_val(self, head: Optional[ListNode]):
    #     if not head: return []
    #     if not head.next: return [head.val]
    #     return [head.val, *self.get_val(head.next)]

    def get_val(self, head: Optional[ListNode]):
        vals = []
        while head:
            vals.append(head.val)
            head = head.next
        return vals

node_one = ListNode(1)
node_two = ListNode(0)
node_tree = ListNode(1)
# node_four = ListNode(3)
# node_five = ListNode(2)
# node_six = ListNode(1)
# node_one = ListNode(7)
# node_two = ListNode(7)
# node_tree = ListNode(7)
# node_four = ListNode(7)

node_one.next = node_two
node_two.next = node_tree
# node_tree.next = node_four
# node_four.next = node_five
# node_five.next = node_six
# node_four.next = node_two


sol = Solution()
print(sol.isPalindrome(node_one))
