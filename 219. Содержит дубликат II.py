from typing import List
from collections import defaultdict

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        hash_map = defaultdict(list)

        for i, num in enumerate(nums):
            hash_map[num].append(i)

        for key in filter(lambda key: len(hash_map[key]) > 1 ,hash_map):
            current_index = hash_map[key][0]
            for i in range(1, len(hash_map[key])):
                if abs(current_index - hash_map[key][i]) <=k:
                    return True
                current_index = hash_map[key][i]
        return False





        print()





sol = Solution()
print(sol.containsNearbyDuplicate(nums = [1,2,3,1], k = 3 ))
print(sol.containsNearbyDuplicate(nums = [1,0,1,1], k = 1 ))
print(sol.containsNearbyDuplicate(nums = [1,2,3,1,2,3], k = 2 ))