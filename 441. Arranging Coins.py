class Solution:
    def arrangeCoins(self, n: int) -> int:
        if n == 1:
            return 0

        for i in range(1,n+1):
            if i > n:
                return i-1
            n -= i



sol = Solution()
assert sol.arrangeCoins(1) == 0
assert sol.arrangeCoins(5) == 2
assert sol.arrangeCoins(8) == 3
