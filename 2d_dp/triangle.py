from typing import List
class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        """
        Qual vai ser a minha dp:
        Eu armazeno a menor soma da linha atual.

        Tem que ter cuidado porque pode ter um caso assim:
               -1
                2  3
                1 -1  3
        Eu vou ter uma matriz que vai me dar a menor soma -> Linhas: Linha do triangulo
                                                          -> Colunas: Menor soma para chegar naquele numero
        Resposta: O menor valor da última linha
        Como eu cheguei nessa linha de raciocínio: Eu percebi que eu preciso saber "todas" as opções, pois pode acontecer
        de haver um numero muito grande no fim mas com um caminho barato
        """

        dp = [[-99999 for _ in range(len(triangle[i]))] for i in range(len(triangle))]
        # print(dp)
        dp[0][0] = triangle[0][0]
        for idx_linha in range(1, len(triangle)):
            for idx_coluna in range(len(triangle[idx_linha])):
                # print(f'linha: {idx_linha}; coluna: {idx_coluna}')
                value = triangle[idx_linha][idx_coluna]
                max_idx_anterior = len(triangle[idx_linha-1]) - 1
                dp[idx_linha][idx_coluna] = min(dp[idx_linha-1][min(max_idx_anterior, idx_coluna)], dp[idx_linha-1][max(0, idx_coluna - 1)]) + value
        # print(dp)
        response = 99999
        for value in dp[-1]:
            if value != -99999:
                response = min(response, value)
        return response
print(Solution().minimumTotal(triangle = [[-1],[2,3],[1,-1,-3]]))