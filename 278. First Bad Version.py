# The isBadVersion API is already defined for you.
def isBadVersion(version: int) -> bool:
    return version >= 22


class Solution:
    def firstBadVersion(self, n: int) -> int:
        versions = [i for i in range(1, n+1)]
        while len(versions) > 2:
            n = n//2 if n // 2 else n % 2
            check = isBadVersion(versions[n])
            if check:
                versions = versions[:n+1]
            else:
                versions = versions[n:]
        if isBadVersion(versions[0]):
            return versions[0]
        else:
            return versions[1]




    def firstBadVersion(self, n: int) -> int:
        start = 0
        end = n
        while start != end:
            i = int(start + (end-start) / 2)
            if not isBadVersion(i):
                start = i+1
            else:
                end = i
        return end











sol = Solution()
assert sol.firstBadVersion(n = 30) == 22
assert sol.firstBadVersion(n = 1) == 1
