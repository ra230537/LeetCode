from typing import List
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        '''
        Input: candidates = [2,3,5], target = 8
        Output: [[2,2,2,2],[2,3,3],[3,5]]
        para cada numero
        adiciona na lista de possibilidades da vez
        diminui o target pelo valor escolhido
        se o valor for maior que 0, continua recursivamente 
        se o valor for 0, retorna o valor
        se o for menor que 0, passa pro proximo
        '''
        global_list = []
        def backtracking(candidates, target, current_number, current_list):
            if target - current_number < 0:
                return None
            elif target == current_number:
                current_list.append(current_number)
            else:
                for idx in range(len(candidates)):
                    current_candidate = candidates[idx]
                    result = backtracking(candidates, target - current_candidate, current_candidate, current_list)
                    if result is None:
                        continue
                    current_list.append(result)
            print(current_list)
            return current_list
        return backtracking(candidates, target, 0,[])
Solution().combinationSum(candidates = [2,3,5], target = 8)