class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) < 2: return s
        i = 0
        j = 1
        pals = ["", s[i]]
        while i < len(s):
            res = s[i]
            while j < len(s):
                res += s[j]
                if res == res[::-1]:
                    pals.append(res)
                j += 1
            i += 1
            j = i + 1
        return max(pals, key=lambda i: len(i))


    def longestPalindrome(self, s: str) -> str:
        size = len(s)
        start = 0
        end = 0
        for i in range(size):
            for j in range(2):
                left = i
                right = i + j
                while left >= 0 and right <= (size - 1) and s[left] == s[right]:
                    left -= 1
                    right += 1
                left += 1
                right -= 1
                if right - left > end - start:
                    start = left
                    end = right
        return s[start:end + 1]



sol = Solution()
# print(sol.longestPalindrome("ac"))
# print(sol.longestPalindrome("babad"))
print(sol.longestPalindrome("cbbd"))