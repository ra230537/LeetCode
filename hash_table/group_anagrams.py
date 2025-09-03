from typing import List
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Ordenado: [desordenado]
        response = {}
        response_list = []
        for word in strs:
            sorted_word = ''.join(sorted(word))
            if sorted_word not in response:
                response[sorted_word] = []
            response[sorted_word].append(word)
        for key in response.keys():
            response_list.append(response[key])
        return response_list
    
print(Solution().groupAnagrams(strs = ["eat","tea","tan","ate","nat","bat"]))