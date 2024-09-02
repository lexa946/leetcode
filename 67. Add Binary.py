class Solution:
    def addBinary(self, a: str, b: str) -> str:
        a = int(a, 2)
        b = int(b, 2)
        res = a+b
        res = bin(res)
        return res[2:]


        a = [int(digit) for digit in a]
        b = [int(digit) for digit in b]
        c = []
        v_ume = False

        for i in range(1, max(len(a), len(b))+1):
            try:
                cur_a = a[-i]
            except IndexError:
                cur_a = 0

            try:
                cur_b = b[-i]
            except IndexError:
                cur_b = 0

            if v_ume:
                cur_a += 1
                v_ume = False

            cur_c = cur_a + cur_b

            if cur_c == 2:
                c.append('0')
                v_ume = True
            elif cur_c == 3:
                c.append('1')
                v_ume = True
            elif cur_c == 1:
                c.append('1')
            else:
                c.append('0')

        if v_ume:
            c.append('1')
        c.reverse()
        return "".join(c)






sol = Solution()
print(sol.addBinary(a = "11", b = "1"))
print(sol.addBinary(a = "1010", b = "1011"))
# print(sol.addBinary())