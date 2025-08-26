'''
Eu vou guardar até onde o meu vetor consegue chegar
Se o meu indice atual for maior que o meu valor maximo, retorno false: Eu não conseguiria chegar la passando por onde eu passei
Se a soma entre o meu indice atual + v[idx] > valor maximo -> atualizo o valor maximo
Se o meu valor máximo for igual ao tamanho do array -1 -> retorno verdade
'''
from typing import List
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        max_idx = 0
        size = len(nums)
        for idx in range(size):
            if (idx > max_idx):
                return False
            if (idx + nums[idx] > max_idx):
                max_idx = idx + nums[idx]
            if (max_idx >= size - 1):
                return True
        return False
print(Solution().canJump(nums = [2,3,1,1,4]))