from typing import List
class Solution:
    def rob(self, nums: List[int]) -> int:
        response = [0 for _ in range(len(nums))]
        # tem que verificar se não da out of range
        response[0] = nums[0]
        response[1] = nums[1]
        max_val = -1
        for i in range(2, len(nums)):
            # tem que verificar se não da out of range
            response[i] = max(nums[i]+ response[i-2], nums[i]+response[i-3])
            #talvez ter um contador de maximo aqui p controlar o fluxo
        return max_val