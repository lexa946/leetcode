
class Solution:
    def scoreOfString(self, s: str) -> int:
        scores_chr = [ord(char) for char in s]
        scores = []
        while len(scores_chr) > 1:
            last_score_char = scores_chr.pop()
            scores.append(abs(last_score_char-scores_chr[-1]))

        return sum(scores)




sol = Solution()
assert sol.scoreOfString("hello") == 13
assert sol.scoreOfString("zaz") == 50