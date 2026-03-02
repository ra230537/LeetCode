from typing import List
import heapq
'''
uso de heap minimo com negativo pra pegar o maior
'''
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.nums = list(map(lambda x: -x, nums))
        self.k = k
    def add(self, val: int) -> int:
        heapq.heappush(self.nums, -val)
        return -heapq.nsmallest(self.k, self.nums)[-1]
ktl = KthLargest(3, [1, 3, 2])
print(ktl.add(5))