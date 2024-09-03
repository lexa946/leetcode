class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        map_a = {}
        map_b = {}
        res = True


        for char_a, char_b in zip(s, t):
            if char_a not in map_a:
                map_a[char_a] = char_b
            if map_a[char_a] != char_b:
                res = False

            if char_b not in map_b:
                map_b[char_b] = char_a
            if map_b[char_b] != char_a:
                res = False

        return res



sol = Solution()
sol.isIsomorphic(s = "egg", t = "add")
sol.isIsomorphic(s = "foo", t = "bar")
sol.isIsomorphic(s = "paper", t = "title")
sol.isIsomorphic(s = "badc", t = "baba")
