from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = 0
        count = 0
        while count < len(nums):
            if nums[i] == 0:
                nums.append(nums.pop(i))
            else:
                i += 1
            count += 1


sol = Solution()
nums = [0,1,0,3,12]
sol.moveZeroes(nums = nums)
assert nums == [1,3,12,0,0]



