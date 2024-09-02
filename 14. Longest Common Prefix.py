from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # out_str = ""
        #
        # min_range = min(strs, key=lambda str_: len(str_))
        # for i in range(len(min_range)):
        #     set_temp = set(str[i] for str in strs)
        #     if len(set_temp) > 1: break
        #     else: out_str += strs[0][i]
        # return out_str
        #


        if not strs:
            return ""

        prefix = strs[0]

        for string in strs[1:]:
            while string[:len(prefix)] != prefix and prefix:
                prefix = prefix[:-1]

        return prefix
        print()





sol = Solution()
print(sol.longestCommonPrefix(["flower","flow","flight"]))
print(sol.longestCommonPrefix(["dog","racecar","car"]))