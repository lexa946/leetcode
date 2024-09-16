from itertools import zip_longest


class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        map_left = {}
        map_right = {}
        words = s.split()

        if len(words) != len(pattern):
            return False


        for char, word in zip(pattern, words):
            if char in map_left and map_left[char] != word:
                return False
            elif word in map_right and map_right[word] != char:
                return False
            else:
                map_left[char] = word
                map_right[word] = char

        return True

    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split()

        set_pattern = set(pattern)
        set_words = set(words)
        set_longers = set(zip_longest(words, pattern))

        if len(set_words) == len(set_pattern) == len(set_longers):
            return True
        else:
            return True






sol = Solution()
assert sol.wordPattern(pattern = "aba", s = "dog cat cat") == True
assert sol.wordPattern(pattern = "abba", s = "dog cat cat dog") == True
assert sol.wordPattern(pattern = "abba", s = "dog dog dog dog") == False
assert sol.wordPattern(pattern = "abba", s = "dog cat cat fish") == False