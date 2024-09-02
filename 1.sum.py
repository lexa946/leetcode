from typing import List


# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
#         for i in range(len(nums)):
#             for j in range(len(nums)):
#                 if i == j: continue
#                 if nums[i] + nums[j] == target:
#                     return [i, j]
#


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map = {}

        for i, num in enumerate(nums):
            # if target - num in map:
            #     return [i, map[target - num]]
            map[num] = i

        print(i,num)



solution = Solution()
solution.twoSum([2,11,7,15], 9)