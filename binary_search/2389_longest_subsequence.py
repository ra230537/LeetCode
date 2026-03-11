from typing import List
import bisect
'''
UTILIDADE: Biblioteca bisect é muito importante para ganhar tempo em problemas de busca binária, importantíssimo não implementar uma busca binária
quando não for o cerne da questão
'''

class Solution:
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        nums.sort()
        response = []
        array_sum = []
        current_sum = 0
        for num in nums:
            current_sum += num
            array_sum.append(current_sum)
        for query in queries:
            index = bisect.bisect_right(array_sum, query)
            response.append(index)
        return response
print(Solution().answerQueries(nums = [4,5,2,1], queries = [3,10,21]))