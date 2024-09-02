from collections import Counter
from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        last_max = nums[0]
        uniq_index = 1
        for i in range(1, len(nums)):
            if nums[i] > last_max:
                digit = nums.pop(i)
                nums.insert(uniq_index, digit)
                uniq_index += 1
                last_max = digit
        return uniq_index


sol = Solution()

print(sol.removeDuplicates(nums = [1,1,2]))
print(sol.removeDuplicates(nums = [0,0,1,1,1,2,2,3,3,4]))
# print(sol.removeDuplicates())
# print(sol.removeDuplicates())