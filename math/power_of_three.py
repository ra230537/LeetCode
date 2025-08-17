class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if (n < 1):
            return False
        if (3486784401 % n == 0):
            return True
        return False
    