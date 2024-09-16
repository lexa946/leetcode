from typing import List
from collections import Counter


class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        counter_nus_1 = Counter(nums1)
        counter_nus_2 = Counter(nums2)
        res = []

        for key in counter_nus_1:
            if key not in counter_nus_2:
                continue
            res.extend(
                [key] * min(counter_nus_2[key], counter_nus_1[key])
            )

        return res


sol = Solution()
assert sol.intersect(nums1 = [1,2,2,1], nums2 = [2,2]) == [2, 2]
assert sol.intersect(nums1 = [4,9,5], nums2 = [9,4,9,8,4]) == [9, 4]