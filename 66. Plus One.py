from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        #
        # length_digits = len(digits)
        # digits[-1] += 1
        # proyadok = False
        #
        # for i in range(1, length_digits+1):
        #     if proyadok:
        #         digits[-i] += 1
        #         proyadok = False
        #     if digits[-i] == 10:
        #         proyadok = True
        #         digits[-i] = 0
        # if proyadok:
        #     digits.insert(0, 1)
        # return digits

        str_d = "".join(str(digit) for digit in digits)
        str_d = str(int(str_d)+1)
        digits = [int(digit) for digit in str_d]
        return digits





sol = Solution()
print(sol.plusOne([1, 2, 3]))
print(sol.plusOne([4, 3, 2, 1]))
print(sol.plusOne([9]))
print(sol.plusOne([9, 9]))
