from typing import List
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        response = ""
        min_word_size = min(map(lambda x: len(x), strs))
        for idx_letter in range(min_word_size):
            for idx_word in range(len(strs)-1):
                if(strs[idx_word][idx_letter] != strs[idx_word + 1][idx_letter]):
                    return response
            response+=strs[0][idx_letter]
        return response
print(Solution().longestCommonPrefix( strs = ["dog","racecar","car"]))