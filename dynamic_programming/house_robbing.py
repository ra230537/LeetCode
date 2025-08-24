from typing import List
'''
Ou você decide roubar duas casas para tras e atual ou 3 casas para tras e a atual
Não pode roubar uma casa pra tras porque soa o alarme
e não faz sentido roubar 4 casas pra tras, porque eh melhor roubar 2 casas pra tras e depois 2 casas pra tras dessa

'''
class Solution:
    def rob(self, nums: List[int]) -> int:
        # dinheiro maximo robando a casa k
        nums_size = len(nums) 
        response = [0 for _ in range(nums_size)]

        # tem que verificar se não da out of range
        response[0] = nums[0]
        if nums_size > 1:
            response[1] = nums[1]
        if nums_size > 2:
            response[2] = nums[2] + nums[0]
        max_val = max(response)
        for i in range(3, len(nums)):
            # [x, x, x, x, x, x]
            response[i] = max(nums[i]+ response[i-2], nums[i]+response[i-3])
            max_val = max(max_val, response[i])
        return max_val
print(Solution().rob([2, 7, 6]))