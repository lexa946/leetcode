class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if not n:
            return False
        for i in range(1, n):
            mod = i**3
            if mod > n:
                break
            if mod == n:
                return True
        return False


    def isPowerOfThree(self, n: int) -> bool:
        if not n:
            return False
        while (n -1):
            if n % 3 != 0:
                return False
            n = n//3
        return True






sol = Solution()
assert sol.isPowerOfThree(9) == True
assert sol.isPowerOfThree(27) == True
assert sol.isPowerOfThree(0) == False
assert sol.isPowerOfThree(1) == False
