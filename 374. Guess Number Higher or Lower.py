# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:
def guess(num: int) -> int:
    pick = 2
    if num < pick:
        return 1
    elif num > pick:
        return -1
    else:
        return 0



class Solution:
    def guessNumber(self, n: int) -> int:
        left_border = 1
        right_border = n

        while left_border != right_border:
            middle_num = (left_border+right_border) //2

            direction = guess(middle_num)
            if direction == -1:
                right_border = middle_num
            elif direction == 1:
                left_border = middle_num+1
            else:
                return middle_num

        return n



sol = Solution()
assert sol.guessNumber(n = 2) ==  2
assert sol.guessNumber(n = 1) ==  1
assert sol.guessNumber(n = 10) ==  6
