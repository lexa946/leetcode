class Solution:
    def reverseBits(self, n: int) -> int:
        bin_n = int(bin(n)[::-1], 2)
        n = int(str(n)[::-1])

        res = 0
        for i, char in enumerate(str(n)[::-1]):
            number = int(char)
            res += number * 2**i
        print()

        return res


sol = Solution()
# print(sol.reverseBits(10100101000001111010011100))
print(sol.reverseBits(1111111111111111111111111101))
