from typing import List

'''
Uma solução mais elegante seria ter um prefixo e um posfixo (variaveis)
O prefixo seria o acumulado da multiplicação dos valores passados exceto o valor atual, dai iriamos multiplicando o prefixo a cada passageme e multiplicando por 1
e guardando

Depois fariamos o mesmo para o posfixo, pois no prefixo teriamos multiplicado por tudo da esquerda e no posfixo precisariamos multiplicar por tudo da direita


'''
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        size = len(nums)
        foward = [nums[idx] for idx in range(size)]
        backward = [nums[idx] for idx in range(size)]
        for idx in range(1, size):
            foward[idx] = foward[idx] * foward[idx-1]
        for idx in range(size-2,-1,-1):
            backward[idx] = backward[idx] * backward[idx+1]
        response = [0 for _ in range(size)]
        for idx in range(size):
            foward_value = 1
            backward_value = 1
            if (idx > 0):
                foward_value = foward[idx-1]
            if (idx < size-1):
                backward_value = backward[idx+1]
            response[idx] = foward_value * backward_value
        return response
print(Solution().productExceptSelf(nums = [-1,1,0,-3,3]))