from typing import List
from collections import Counter


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        counter = Counter(nums)
        return {value:key for key, value in counter.items()}[1]




sol = Solution()
assert sol.singleNumber([2,2,1]) == 1
assert sol.singleNumber([4,1,2,1,2]) == 4
assert sol.singleNumber([1]) == 1