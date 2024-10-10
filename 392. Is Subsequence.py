class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if not s:
            return True

        s_arr = list(s)

        for char_ in t[::-1]:
            if char_ == s_arr[-1]:
                s_arr.pop()
            if not s_arr:
                return True
        return False



sol = Solution()

assert sol.isSubsequence("b", "abc") == True
assert sol.isSubsequence("abc", "ahbgdc") == True
assert sol.isSubsequence("axc", "ahbgdc") == False