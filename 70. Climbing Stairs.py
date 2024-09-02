class Solution:
    counter = 0

    def climbStairs(self, n: int) -> int:
        a, b = 0, 1
        for i in range(n):
            a, b = b, a + b
        return b




sol = Solution()
# print(sol.climbStairs(2))
print(sol.climbStairs(4))
print(sol.climbStairs(3))
