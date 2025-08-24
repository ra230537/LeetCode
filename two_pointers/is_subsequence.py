class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i = 0
        j = 0
        size_s = len(s)
        size_t = len(t)
        if (len(t) < len(s)):
            return False
        while i<size_s and j < size_t:
            if s[i] == t[j]:
                i+=1
            j+=1
        if i == size_s:
            return True
        else:
            return False