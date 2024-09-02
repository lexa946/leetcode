from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


    def __repr__(self):
        return f"{self.val}"

class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        if not nums: return None

        zero_index = int(len(nums)/2)
        tree_node = TreeNode(val=nums[zero_index])
        left_arr = nums[:zero_index]
        right_arr = nums[zero_index+1:]
        tree_node.left = self.sortedArrayToBST(left_arr)
        tree_node.right = self.sortedArrayToBST(right_arr)

        return tree_node








sol = Solution()
# print(sol.sortedArrayToBST(nums = [-10,-3,0,5,9]))
test = sol.sortedArrayToBST(nums = [5,4,8,11,13,4,7,2,1])
print()
print(sol.sortedArrayToBST(nums = [-10,-3]))