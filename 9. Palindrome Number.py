class Solution:
    def isPalindrome(self, x: int) -> bool:

        if str(x) == str(x)[::-1]:
            return True

        return False




sol = Solution()
print(sol.isPalindrome(-121))