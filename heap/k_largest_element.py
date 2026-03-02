from typing import List
import heapq
'''
Para achar o mais largo, basta usar a tecnica de deixar todos negativos
Buscar os k menores.
O Maior vai ser o 0 negativo
enquanto o k enor vai ser o negativo do ultimo
'''
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums = list(map(lambda x: -x, nums))
        heapq.heapify(nums)
        response = heapq.nsmallest(k, nums)
        return -response[-1]