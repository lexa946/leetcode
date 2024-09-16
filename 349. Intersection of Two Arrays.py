from typing import List


class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        set_one = set(nums1)
        set_two = set(nums2)
        res = list(set_one & set_two)
        return res



sol = Solution()
assert sol.intersection(nums1 = [4,9,5], nums2 = [9,4,9,8,4]) == [4,9]
assert sol.intersection(nums1 = [1,2,2,1], nums2 = [2,2]) == [2]
