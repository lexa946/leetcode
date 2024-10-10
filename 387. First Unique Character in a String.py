from collections import defaultdict

class Solution:
    def firstUniqChar(self, s: str) -> int:
        counter = defaultdict(list)
        for i,char_ in enumerate(s):
            counter[char_].append(i)
        for value in counter.values():
            if len(value) == 1:
                return value[0]
        return -1


sol = Solution()
assert sol.firstUniqChar("loveleetcode") == 2
assert sol.firstUniqChar("leetcode") == 0
assert sol.firstUniqChar("aabb") == -1
