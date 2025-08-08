# The isBadVersion API is already defined for you.
bad = 1
def isBadVersion(version: int) -> bool:
    return version >= bad
    
class Solution:
    def firstBadVersion(self, n: int) -> int:
        teto = n
        piso = 1
        bad_version = teto
        while (teto >= piso):
            meio = (teto + piso) // 2
            if (isBadVersion(meio)):
                teto = meio - 1
                bad_version = meio
            else:
                piso = meio + 1
        return bad_version
print(Solution().firstBadVersion(1))
