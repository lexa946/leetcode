class Solution:
    symbols_close = {
        '{': '}', '[': ']', '(': ')',
    }

    symbols_open = ['(', '[', '{']
    #
    # def isValid(self, s: str, open_symbol=None) -> bool:
    #     if len(s) % 2 != 0: return False
    #
    #     stack = []
    #     for symbol in s:
    #         if symbol in self.symbols_open:
    #             stack.append(symbol)
    #         else:
    #             if not stack:
    #                 return False
    #             last_open = stack.pop()
    #             if symbol != self.symbols_close[last_open]:
    #                 return False
    #
    #     if stack:
    #         return False
    #     return True

    def isValid(self, s: str, open_symbol=None) -> bool:
        if len(s) == 1:
            return False


        stack = [s[0]]


        for char in s[1:]:
            if char in [')', ']', '}'] and len(stack):
                openBracket = stack.pop()
                if char == ')' and openBracket != '(':
                    return False
                if char == ']' and openBracket != '[':
                    return False
                if char == '}' and openBracket != '{':
                    return False
            else:
                stack.append(char)
        return len(stack) == 0


sol = Solution()
# print(sol.isValid("["))
# print(sol.isValid("(("))
print(sol.isValid("){"))
print(sol.isValid("()"))
print(sol.isValid("()[]{}"))
print(sol.isValid("[)(]{}"))
print(sol.isValid("(]"))
print(sol.isValid("([])"))
print(sol.isValid("([])"))
