class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        if int(num**0.5)**2==num:
            return True
        else:
            return False



sol = Solution()
assert sol.isPerfectSquare(16) == True
assert sol.isPerfectSquare(14) == False
