class Solution:
    def romanToInt(self, s: str) -> int:
        map = {
            "I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000,
        }
        digits = [map[letter] for letter in s]
        counter = 0
        for i in range(len(digits)):
            digit_one = digits.pop()
            if digits:
                if digit_one > digits[-1]:
                    deleter = digits.pop()
                    counter -= deleter
            counter += digit_one
            if not digits: break
        return counter


sol = Solution()
print(sol.romanToInt("MCDLXXVI"))
