from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


    def __repr__(self):
        return f"{self.val}"



class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root: return False

        targetSum -= root.val
        if targetSum == 0 and not root.left and not root.right:
            return True
        has_path_left = False
        has_path_right = False
        if root.left:
            has_path_left = self.hasPathSum(root.left, targetSum)
        if root.right:
            has_path_right = self.hasPathSum(root.right, targetSum)
        return has_path_right or has_path_left





    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        if not nums: return None

        zero_index = int(len(nums)/2)
        tree_node = TreeNode(val=nums[zero_index])
        left_arr = nums[:zero_index]
        right_arr = nums[zero_index+1:]
        tree_node.left = self.sortedArrayToBST(left_arr)
        tree_node.right = self.sortedArrayToBST(right_arr)

        return tree_node





if __name__ == '__main__':
    sol = Solution()
    test = sol.sortedArrayToBST(nums = [-2, -3])
    print(sol.hasPathSum(test, -5))