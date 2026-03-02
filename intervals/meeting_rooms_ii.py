"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""
from typing import List, Tuple
class Solution:
    def minMeetingRooms(self, intervals: List[Tuple]) -> int:
        # Vou criar uma lista de intervalos, cada item só vai ter um tamanho que pode ser modificado pra crescer
        hour_list = []
        intervals.sort(key=lambda x: (x[0],x[1]))
        '''
        Para cada intervalo da lista
            Para cada horario na minha lista de horarios
                Verfificar se é possível encaixar com o intervalo com menor fim possivel
                Se for possível, encaixar
                Se não for possível, criar um novo
        retorna o tamanho do hour_list
        '''
        for i, interval in enumerate(intervals):
            cur_start = interval[0]
            cur_end = interval[1]
            for j, hour in enumerate(hour_list):
                cur_hour_end = hour[1]
                if (cur_start >= cur_hour_end):
                    hour_list[j][1] = cur_end
                    break
            else:
                hour_list.append([cur_start, cur_end])
        print(hour_list)
        return len(hour_list)
print(Solution().minMeetingRooms([(0,40),(5,10),(15,20)]))
# intervals = [(0,40),(5,10),(15,20)]
'''
Sempre escrever o algoritmo em alto nivel
eu dei um sort
EU verifiquei que eu não conseguiria saber de todas as salas sem salvar elas antes, então eu salvo ela
Dai eu só verifico se eu preciso modificar o valor ou não do intervalo
'''