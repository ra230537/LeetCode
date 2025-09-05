from typing import List
'''
TODO: ANOTAR COMO USAR KEY DO SORTED
Solução: Eu verifico se o inicio do atual é menor ou igual ao conjunto corrente
Se for, eu vejo quem tem o maior final e atualizo o conjunto corrente
Se não for, como o intervalo tá ordenado eu tenho certeza que ninguém na frente vai ser também então eu posso criar um novo intervalo correntes
'''
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals = sorted(intervals, key=lambda x: x[0])
        print(intervals)
        response = [intervals[0]]
        for idx in range(1, len(intervals)):
            if (intervals[idx][0] <= response[-1][1]):
                response[-1][1] = max(intervals[idx][1], response[-1][1])
            else:
                response.append(intervals[idx])
        return response
print(Solution().merge(intervals = [[2,3],[4,5],[6,7],[8,9],[1,10]]))