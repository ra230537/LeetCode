from typing import List
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        response = [[1]]
        # repete n -1 vezes
        for _ in range(numRows-1):
            # Busca a ultima linha
            row = response[-1]
            # inicializa com 1
            new_row = [1]
            # para cada elemento, soma ele mesmo com o proximo e adiciona na resposta da nova linha
            for idx in range(len(row)-1):
                new_row.append(row[idx] + row[idx + 1])
            # poe um no fim
            new_row.append(1)
            # compoe a resposta final com a resposta da linha
            response.append(new_row)
        return response
print(Solution().generate(1))