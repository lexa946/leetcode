# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right



class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root: return 0
        # depth = 0
        if not root.left and not root.right:
            return 1
        else:
            depth = []
            if root.left:
                depth.append(self.maxDepth(root.left))
            if root.right:
                depth.append(self.maxDepth(root.right))

            return 1 + max(depth)












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






sol = Solution()
# print(sol.maxDepth(mirror))
print(sol.maxDepth(node_one))
