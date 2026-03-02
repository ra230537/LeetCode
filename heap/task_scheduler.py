from typing import List, Dict
import heapq
'''
Eu vou precisar saber quantos ciclos vão demorar
a restrição é que a mesma letra precisa esfriar por n ciclos pra poder rodar dnv
Eu pensei em ter um heapq de 26 posições em que cada posição é uma letra.
cada um começa com valor 0 pois todos estão frios
Eu só posso escolher as letras com cooldown 0 e tenho que usar como critério a letra que tem mais aparições
Eu preciso ter um dicionario para cada letra mostrando também as aparicções
Sempre eu escolher uma letra eu preciso alterar o cooldown dela no heap e diminuir uma aparição dela no hash
também diminuir em um no cooldown de todas as outras letras no heap

O problema é: como encontrar as letras com 0 aparições de forma fácil?
{letra: [aparicoes, cooldown]}
Podia ter feito melhor, usando maxheap pra pegar as maiores apariçoes com cooldown 0

'''
class Solution:
    def find_most_repeated_fresh(self, dict_lookup: Dict[str, List[int]]):
        response_key = -1
        max_ocurrences = 0
        for key, value in dict_lookup.items():
            ocurrences = value[0]
            cooldown = value[1]
            if (cooldown == 0):
                if ocurrences > max_ocurrences:
                    max_ocurrences = ocurrences
                    response_key = key
        return response_key
    def cool(self, dict_lookup: Dict[str, List[int]]):
        for key, values in dict_lookup.items():
            dict_lookup[key][1] = max(0, dict_lookup[key][1] - 1)
        return dict_lookup
    def warm(self, dict_lookup: Dict[str, List[int]], key, n):
        dict_lookup = self.cool(dict_lookup)
        dict_lookup[key][1] = n
        dict_lookup[key][0] = max(0, dict_lookup[key][0]-1)
        return dict_lookup
    def print_dict(self, dict_lookup: Dict[str, List[int]]):
        dictionary = {}
        for key, values in dict_lookup.items():
            if values != [0, 0]:
                dictionary[key] = values
        print(dictionary)
    def leastInterval(self, tasks: List[str], n: int) -> int:
        dict_lookup = {i: [0, 0] for i in range(26)}
        for task in tasks:
            idx_task = ord(task) - ord('A')
            dict_lookup[idx_task][0] += 1
        response = 0
        size_input = len(tasks)
        while size_input > 0:
            key = self.find_most_repeated_fresh(dict_lookup)
            # Não conseguiu nada fresco
            response += 1
            print(f'Chave usada: {key}')
            self.print_dict(dict_lookup)
            if (key == -1):
                dict_lookup = self.cool(dict_lookup)
                continue
            dict_lookup = self.warm(dict_lookup, key, n)
            size_input -= 1
        return response
print(Solution().leastInterval(tasks = ["A","A","A","B","C"], n = 3))