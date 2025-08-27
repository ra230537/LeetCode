'''
Eu vou guardar até onde o meu vetor consegue chegar
Se o meu indice atual for maior que o meu valor maximo, retorno false: Eu não conseguiria chegar la passando por onde eu passei
Se a soma entre o meu indice atual + v[idx] > valor maximo -> atualizo o valor maximo
Se o meu valor máximo for igual ao tamanho do array -1 -> retorno verdade
'''
from typing import List
class Solution:
    def jump(self, nums: List[int]) -> bool:
        max_idx = nums[0]
        temp_max_idx = nums[0]
        count_jumps = 0
        size = len(nums)
        # print(f'Indice maximo: {size-1}')
        for idx in range(size-1):
            # Guarda um valor temporario até que o indice do pulo máximo tenha acabado
            if (idx + nums[idx] > temp_max_idx):
                temp_max_idx = idx + nums[idx]
            # Quando estamos no valor do indice maximo, podemos atualizar o novo indice maximo e indicar que aconteceu um pulo ao numero que causou esse indice
            if (idx == max_idx):
                max_idx = temp_max_idx
                count_jumps += 1
            # Caso chegue no final, ok finalizamos e damos um ultimo pulo
            # Isso foi mais um caso de borda, acho que o ideal seria ter um caso de borda para size = 0, e não fazer range(size-1) e esse count_jump embaixo
            if (max_idx >= size - 1):
                count_jumps += 1
                return count_jumps
        return count_jumps
print(Solution().jump(nums = [1,2,3]))