from collections import Counter

class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        counter_s = Counter(s)
        counter_t = Counter(t)
        counter_x = counter_t-counter_s
        return list(counter_x.keys())[0]


sol = Solution()
assert sol.findTheDifference(s="ab", t="aba") == "a"
assert sol.findTheDifference(s="abcd", t="abcde") == "e"
assert sol.findTheDifference(s="", t="y") == "y"
