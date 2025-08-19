class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        t_size = [0 for _ in range(26)]
        s_size = [0 for _ in range(26)]
        for letter in s:
            s_size[ord(letter)-ord('a')]+=1
        for letter in t:
            t_size[ord(letter)-ord('a')]+=1
        for s, t in zip(s_size, t_size):
            if s!=t:
                return False
        return True