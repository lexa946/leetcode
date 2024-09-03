class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s: return 0
        max_length = 1
        cur_sub = s[0]
        i = 0
        j = 1
        while i < len(s) - 1:

            while j < len(s):
                if s[j] not in cur_sub:
                    cur_sub += s[j]
                    j += 1
                else:
                    if max_length < len(cur_sub):
                        max_length = len(cur_sub)

                    i += 1

                    cur_sub = s[i]
                    break
            j = i + 1
        return max_length

    def lengthOfLongestSubstring(self, s: str) -> int:
        res = 0
        l = 0
        n = len(s)
        sett = set()
        for r in range(n):
            while s[r] in sett:
                sett.remove(s[l])
                l += 1
            sett.add(s[r])
            lon = r - l + 1
            res = max(res, lon)
        return res


sol = Solution()
print(sol.lengthOfLongestSubstring(""))
print(sol.lengthOfLongestSubstring("abcabcbb"))
print(sol.lengthOfLongestSubstring("bbbbbbb"))
print(sol.lengthOfLongestSubstring("pwwkew"))
