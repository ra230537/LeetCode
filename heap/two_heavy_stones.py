from typing import List
import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        '''
        Eu pensei em usar heap porque falou de algo que era o mais pesado ou o mais leve, ese é o padrão
        Como as duas pedras são as mais pesadas, vamos ter que usar o heap pra isso.
        Transformar a lista num heap
        Enquanto o tamanho for maior que um
            remove a maior
            remove a segunda maior
            aplica a logica do problema
        se tiver tamanho 1
            retorna o tamanho
        retorna 0
        '''
        stones = list(map(lambda x: -x, stones))
        heapq.heapify(stones)
        while len(stones) > 1:
            first_minor = -heapq.heappop(stones)
            second_minor = -heapq.heappop(stones)
            result = first_minor - second_minor
            if result != 0:
                heapq.heappush(stones, -result)
        if len(stones) == 1:
            return -stones[0]
        return 0
        