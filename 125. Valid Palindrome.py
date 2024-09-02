
class Solution:
    def isPalindrome(self, s: str) -> bool:
        if s in  (" " ,"."): return True

        list_s = [char.lower() for char in s if char.isalpha() or char.isdigit()]



        str_1 = "".join(list_s)
        str_2 = "".join(list_s[::-1])

        return str_1 == str_2







sol = Solution()
print(sol.isPalindrome(s = "ab2a"))
print(sol.isPalindrome(s = "0P"))
print(sol.isPalindrome(s = ".,"))
print(sol.isPalindrome(s = "A man, a plan, a canal: Panama"))
