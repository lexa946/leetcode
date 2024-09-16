from typing import List


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        if n not in nums: return n
        nums.sort()
        n = nums.pop()

        while nums:
            res = n - 1
            if res != nums[-1]:
                return res

            n = nums.pop()

        return 0

    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        total_sum = sum(nums)
        expected_sum = n * (n +1) // 2
        missing_sum = expected_sum -  total_sum
        return missing_sum


sol = Solution()
# assert sol.missingNumber([1]) == None
assert sol.missingNumber([3,0,1]) == 2
assert sol.missingNumber([0,1]) == 2
assert sol.missingNumber([9,6,4,2,3,5,7,0,1]) == 8