from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # star_len_numx= len(nums)
        # delete_counter = 0
        # index = 0
        # while True:
        #     if index == len(nums): break
        #
        #     if nums[index] == val:
        #         nums.pop(index)
        #         delete_counter += 1
        #     else:
        #         index += 1
        # return star_len_numx - delete_counter

        l = 0
        for i in nums:
            if i != val:
                nums[l] = i
                l += 1
        return l


sol = Solution()
# print(sol.removeElement(nums = [3,2,2,3], val = 3))
print(sol.removeElement(nums = [0,1,2,2,3,0,4,2], val = 2))