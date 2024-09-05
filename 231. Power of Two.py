class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        i = 0
        current_pow = 0
        while current_pow < n:
            current_pow = pow(2, i)
            if current_pow == n:
                return True

            i += 1
        return False


sol = Solution()
print(sol.isPowerOfTwo(1))
print(sol.isPowerOfTwo(16))
print(sol.isPowerOfTwo(3))