from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        node_passed = []
        if not head: return True


        while True:
            if head in node_passed:
                return True
            else:
                node_passed.append(head)
            if head.next:
                head = head.next
            else:
                return False





node_one = ListNode(1)
node_two = ListNode(2)
node_tree = ListNode(3)
node_four = ListNode(4)

node_one.next = node_two
node_two.next = node_tree
node_tree.next = node_four
# node_four.next = node_two



sol = Solution()
print(sol.hasCycle(node_one))