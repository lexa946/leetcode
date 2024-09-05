


class Solution:
    def addDigits(self, num: int) -> int:
        digit_one = num // 10
        digit_two = num % 10
        res = digit_two + digit_one
        if res // 10 == 0:
            return res
        else:
            return self.addDigits(res)






sol = Solution()
assert sol.addDigits(38) == 2
assert sol.addDigits(0) == 0