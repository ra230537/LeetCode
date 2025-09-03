'''
Nesse problema, dado que o numero maximo de cada valor é 1000 e a quantidade de valores é 5000
Podemos usar o count sort
'''
from typing import List
class Solution:
    def hIndex(self, citations: List[int]) -> int:
        # Nosso vetor de saida com os valores ordenados
        response = [0 for _ in range(len(citations))]


        max_value = max(citations)
        
        # Nosso vetor de contagem
        count_vector =  [0 for _ in range(max_value + 1)]
        
        # Agora vamos contar cada aparição e colocar no vetor de contagem
        for idx in range(len(citations)):
            citation = citations[idx]
            count_vector[citation] += 1
        # [0, 2, 1 , 2, 1 ,2]
        # [1, 2, 3]
        # Agora vamos ajustar a posição relativa de cada item
        for idx in range(1, len(count_vector)):
            count_vector[idx] += count_vector[idx - 1]
        
        # Nesse momento, cada indice de count vector representa o valor, e o valor dentro do array representa o indice do ultimo elemento + 1
        # Porque o vetor começa de 0
        # Vetor ordenado
        # [0, 1, 1, 2, 2, 2]
        # Count vector
        # [1, 3, 6]
        # Ou seja, a posição do último valor 1, vai ser 3 - 1  = 2; A posição do ultimo valor 2 vai ser 6 - 1 = 5

        # Agora precisamos percorrer nosso vetor inicial ao contrário para preservar a ordem
        for idx in range(len(citations) - 1, -1, -1):
            value = citations[idx]
            position = count_vector[value] - 1
            response[position] = value
            # Agora a nova posição desse valor tem que ser um pra trás, já que a posição atual já foi usada
            count_vector[value] -= 1
        # print(response)
        h = 0
        # Agora que já temos ordenado o valor, basta percorrer de trás pra frente
        for idx in range(len(response) - 1, -1, -1):
            if response[idx] < h + 1:
                return h 

            h += 1
        return h
print(Solution().hIndex([1,3,1]))

