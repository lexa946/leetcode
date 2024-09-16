from collections import Counter

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        letter_counter = Counter(ransomNote)
        for letter in magazine:
            if letter in letter_counter:
                letter_counter[letter] -= 1
                if not letter_counter[letter]:
                    del letter_counter[letter]
        if letter_counter:
            return False

        return True







sol = Solution()
assert sol.canConstruct( ransomNote = "aa", magazine = "aab") == True
assert sol.canConstruct(ransomNote = "a", magazine = "b") == False
assert sol.canConstruct(ransomNote = "aa", magazine = "ab") == False
