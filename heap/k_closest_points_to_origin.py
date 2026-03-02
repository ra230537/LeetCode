'''
Falou de K pontos mais proximos eu já tenho que pensar em heap88

'''
from typing import List
import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        distance_list = list(map(lambda x: x[0]**2+x[1]**2, points))
        heapq.heapify(distance_list)
        lookup = {}
        response = []
        k_min = heapq.nsmallest(k, distance_list)
        for point in points:
            squared = point[0]**2+point[1]**2
            # Pra melhorar isso basta usar um set em k_min
            if (squared in k_min):
                response.append(point)
        return response
print(Solution().kClosest(points = [[0,2],[2,0],[2,2]], k = 2))
'''
Eu preciso de alguma forma conseguir correlacionar a minha nova lista com a minha lista antiga
Eu obtenho os k minimos
para cada k, eu percorro a lista de entrada e vejo se ele é igual a raiz quadrada
se for, eu coloco numa lista de saida
'''