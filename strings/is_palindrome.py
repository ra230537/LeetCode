class Solution:
    def isPalindrome(self, s: str) -> bool:
        i = 0
        j = len(s)-1
        while i<j:
            if(not s[i].isalnum()):
                i+=1
                print('oi')
                continue
            if (not s[j].isalnum()):
                j-=1
                continue
                print('tchau')
            if (s[i].lower() != s[j].lower()):
                return False
            i+=1
            j-=1
        return True
print(Solution().isPalindrome("0P"))