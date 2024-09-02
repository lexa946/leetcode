# Definition for a binary tree node.
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        return f"{self.val}"


class Solution:

    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        left = root.left
        right = root.right
        return self.isSameTree(left, right)

    def isSameTree(self, p, q):
        if p == None or q == None:
            return p == q
        return p.val == q.val and self.isSameTree(left, right) and self.isSameTree(right, left)

    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        st_one = []
        st_two = []
        while st_one or p or q:
            while p or q:
                st_one.append(p)
                st_two.append(q)
                try:
                    p = p.left
                    q = q.left
                except AttributeError:
                    return False
            p = st_one.pop()
            q = st_two.pop()
            if p.val != q.val:
                return False
            p = p.right
            q = q.right
        return True

    # def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
    #     st = []
    #     res = []
    #
    #     while root or st:
    #         while root:
    #             st.append(root)
    #             root = root.left
    #
    #         root = st.pop()
    #         res.append(root.val)
    #
    #         root = root.right
    #
    #     return res


three_nodes = []
for i in range(10):
    for j in range(5):
        node = TreeNode(val=i + j)
        three_nodes.append(node)

node_one = three_nodes[0]
node_two = three_nodes[1]
node_3 = three_nodes[2]
node_4 = three_nodes[3]
node_5 = three_nodes[4]
node_6 = three_nodes[5]
node_7 = three_nodes[6]

node_one.left = node_two
node_one.right = node_3
node_two.left = node_4
node_4.right = node_5
node_5.left = node_6
node_6.right = node_7

left = TreeNode(1)
# left = None
right = TreeNode(1)
mirror = TreeNode(0, left=left, right=right)

print()

sol = Solution()
# print(sol.inorderTraversal(node_one))
print(sol.isSymmetric(mirror))
print(sol.isSymmetric(node_one))
