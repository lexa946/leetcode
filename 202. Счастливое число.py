class Solution:
    def isHappy(self, n: int) -> bool:
        digits = [int(i) for i in str(n)]
        ogranichitel = 25
        while ogranichitel:
            res = []
            for i in digits:
                res.append(i**2)
            sum_ = sum(res)
            if sum_ == 1:
                return True
            # elif n**2 == sum_:
            #     return False
            else:
                digits = [int(i) for i in str(sum_)]
            ogranichitel -= 1
        return False


sol = Solution()
print(sol.isHappy(7))
print(sol.isHappy(2))
print(sol.isHappy(19))