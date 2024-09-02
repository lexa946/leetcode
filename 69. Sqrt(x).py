class Solution:
    def mySqrt(self, x: int) -> int:
        if not x: return 0
        prev = 0
        for i in range(1, x+1):
            mul = i*i
            if mul == x:
                return int(i)
            elif mul > x:
                return int(prev)
            prev = i
        print()


sol = Solution()
print(sol.mySqrt(4))
print(sol.mySqrt(8))
print(sol.mySqrt(0))
