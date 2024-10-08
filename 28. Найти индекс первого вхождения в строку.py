class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        try:
            return haystack.index(needle)
        except ValueError:
            return -1


sol = Solution()
print(sol.strStr(haystack = "sadbutsad", needle = "sad"))
print(sol.strStr(haystack = "leetcode", needle = "leeto"))