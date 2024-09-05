from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums1.extend(nums2)
        nums1.sort()
        if len(nums1)%2==0:
            a = nums1[int(len(nums1)/2)]
            b = nums1[int(len(nums1)/2)-1]
            return (a+b)/2
        else:
            return float(nums1[int(len(nums1)/2)])








sol = Solution()
print(sol.findMedianSortedArrays(nums1 = [1,3], nums2 = [2]))
print(sol.findMedianSortedArrays(nums1 = [1,2], nums2 = [3,4]))
# print(sol.findMedianSortedArrays())