class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        ans = []
        while columnNumber:
            columnNumber, n = divmod(columnNumber-1, 26)
            ans += chr(n + ord('A'))

        return "".join(reversed(ans))














sol = Solution()
assert sol.convertToTitle(1) == "A"
assert sol.convertToTitle(28) == "AB"
assert sol.convertToTitle(701) == "ZY"
