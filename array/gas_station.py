from typing import List
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        size = len(gas)
        max_idx = -1
        max_sum = -1
        current_idx = 0
        current_sum = 0
        for i in range(2*size):
            idx = i % size
            # atualiza a current sum
            current_sum += gas[idx] - cost[idx] 
            # Se o valor atual, for menor que 0, não compensa continuar nesse index mais
            # O proximo index vai ser a nossa primeira tentativa de index grande
            # Nossa soma fica zerada
            if current_sum < 0:
                current_sum = 0
                current_idx = idx + 1  
            if (current_sum > max_sum):
                # Atualiza a maior soma e diz quem foi o primeiro indice que tornou essa soma grande
                max_idx = current_idx
                max_sum = current_sum
        i = max_idx
        saldo = 0
        for i in range(max_idx, size + max_idx):
            idx = i % size
            saldo += (gas[idx] - cost[idx])
            if (saldo < 0):
                return -1
        return max_idx

print(Solution().canCompleteCircuit(gas = [2, 3, 4], cost = [3, 4, 3]))
