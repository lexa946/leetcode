from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i = 0
        j = 0
        while n:
            cur_i = nums1[i]
            cur_j = nums2[j]

            if cur_i >= cur_j or i==m:
                nums1.pop()
                nums1.insert(i, cur_j)
                j += 1
                n -= 1
                m += 1
            elif cur_i < cur_j:
                i += 1

        print()


        # return sorted(nums1)



        # while n or m:





nums = [1,2,3,0,0,0]

sol = Solution()
# print(sol.merge(nums1 = [1,2,4,5,6,0], m = 5, nums2 = [3], n = 1))
# print(sol.merge(nums1 = [4,5,6,0,0,0], m = 3, nums2 = [1,2,3], n = 3))
# print(sol.merge(nums1 = [2,0], m = 1, nums2 = [1], n = 1))
# print(sol.merge(nums1 = [-1,0,0,3,3,3,0,0,0], m = 6, nums2 = [1,2,2], n = 3))
print(sol.merge(nums1 = nums, m = 3, nums2 = [2,5,6], n = 3))
print(sol.merge(nums1 = [1], m = 1, nums2 = [], n = 0))
print(sol.merge(nums1 = [0], m = 0, nums2 = [1], n = 1))