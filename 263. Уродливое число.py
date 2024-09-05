class Solution:
    def isUgly(self, n: int) -> bool:
        while n > 1:
            if n % 2 == 0:
                n = n/2
            elif n % 3 == 0:
                n = n/3
            elif n % 5 == 0:
                n = n /5
            else:
                break
        return n == 1



sol = Solution()
assert sol.isUgly(6) == True
assert sol.isUgly(1) == True
assert sol.isUgly(14) == False
assert sol.isUgly(8) == True