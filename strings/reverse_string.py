class Solution:
    def reverseString(self, s: list[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        size = len(s)
        med_size = size//2
        for idx in range(med_size):
            temp = s[idx]
            s[idx] = s[size - idx - 1]
            s[size - idx - 1] = temp
        return s
print(Solution().reverseString(s = ["H","a","n","n","a","h"]))
