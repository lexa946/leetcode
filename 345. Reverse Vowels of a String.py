class Solution:
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']

    def reverseVowels(self, s: str) -> str:
        left_idx = 0
        right_idx = len(s)-1
        arr_str = list(s)



        while left_idx < right_idx:
            if arr_str[left_idx] in self.vowels and arr_str[right_idx] in self.vowels:
                arr_str[left_idx], arr_str[right_idx] = arr_str[right_idx], arr_str[left_idx]
                right_idx -= 1
                left_idx += 1
            elif arr_str[left_idx] in self.vowels:
                right_idx -= 1
            else:
                left_idx += 1
        return "".join(arr_str)











sol = Solution()
assert sol.reverseVowels( s = "hello") == "holle"
assert sol.reverseVowels( s = "leetcode") == "leotcede"