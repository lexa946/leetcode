from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        for i in range(len(nums)):
            if target <= nums[i]:
                return i
        return i +1




sol = Solution()
print(sol.searchInsert(nums = [1,3,5,6], target = 5 ))
print(sol.searchInsert(nums = [1,3,5,6], target = 2 ))
print(sol.searchInsert(nums = [1,3,5,6], target = 7 ))