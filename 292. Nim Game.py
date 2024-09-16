class Solution:
    def canWinNim(self, n: int) -> bool:
        return n%4 != 0



sol = Solution()
assert sol.canWinNim(9) == True
assert sol.canWinNim(6) == True
assert sol.canWinNim(5) == True
assert sol.canWinNim(4) == False
assert sol.canWinNim(1) == True
assert sol.canWinNim(2) == True
