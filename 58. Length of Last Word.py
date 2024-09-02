class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        counter = 0
        for letter in s.strip()[::-1]:
            if letter != " ":
                counter += 1
            else: break
        return counter






sol = Solution()
print(sol.lengthOfLastWord(s = "Hello World"))
print(sol.lengthOfLastWord(s = "   fly me   to   the moon  "))
print(sol.lengthOfLastWord(s = "luffy is still joyboy"))