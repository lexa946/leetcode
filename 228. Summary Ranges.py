from typing import List


class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:

        j = 0
        for i in range(1, len(nums)+1):
            if i == len(nums) or nums[i] != nums[i-1] + 1 :
                yield f"{nums[j]}->{nums[i-1]}" if j != i-1 else str(nums[j])
                j = i




sol = Solution()
# sol.summaryRanges([0,1,2,4,5,7])
print(*sol.summaryRanges([0,1,2,4,6,7]))