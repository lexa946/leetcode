from abc import ABC


from typing import List
from collections import Counter

class Solution:
    def countBits(self, n: int) -> List[int]:
        nums = [0]
        for i in range(1, n+1):
            bin_num = bin(i)
            counter = Counter(bin_num[2:])
            nums.append(counter["1"])

        return nums







sol = Solution()
assert sol.countBits(2) == [0,1,1]
assert sol.countBits(5) == [0,1,1,2,1,2]