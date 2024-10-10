# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        return str(self.val)


class Solution:

    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        res = []
        st = [(root, TreeNode())]
        while st:
            root, parent_root = st.pop()
            if not root.left and not root.right and parent_root.left==root:
                res.append(root.val)
            if root.left:
                st.append((root.left, root))
            if root.right:
                st.append((root.right, root))

        return sum(res)





node_3 = TreeNode(3)
node_9 = TreeNode(9)
node_20 = TreeNode(20)
node_15 = TreeNode(15)
node_7 = TreeNode(7)

node_3.left = node_9
node_3.right = node_20

node_20.left = node_15
node_20.right = node_7


sol = Solution()
sol.sumOfLeftLeaves(node_3)