from typing import List
class Solution:

    '''
    Sacada legal: para verificar se uma lista já está na resposta podemos criar uma chave com os valores da lista de modo a identificar unicamente cada lista
    e pesquisar em tempo constante
    Outra opção seria fazer: tuple(sorted(subsset))

    Outra sacada importante: Não precisamos começar do inicio sempre, so precisamos ver os numeros a frente, porque se um numero atrás fosse usado
    já teriamos pegado a tripla dele ex: a, b e c
    se estamos no b e pegamos a e c. Estamos pegando uma tupla que já foi obtida antes, porque antes já fomos no a então já pegamos a, b e c
    '''
    def two_sum(self, nums: List[int], target: int, start_idx) -> List[List[int]]:
        subset = []
        '''
        Lembrar de verificar se o numero é diferente para não ter respostas duplicadas [-1, -1, 5, 5] target 4
        ter i e j

        se nums[i] + nums[j] > target, j -= 1. OtherWise, i+=1
        '''
        first = 0
        i = start_idx
        size_nums = len(nums)
        j = size_nums - 1

        while i < j: 
            if (nums[i] + nums[j] == target):
                subset.append([nums[i], nums[j], -target])
                i += 1
                # Garanto que eu já acertei a primeira vez e agora eu não preciso ficar verificando se eh > 0
                while i < j and nums[i] == nums[i - 1]:
                    i += 1
                j -= 1
                # Analogamente eu não preciso verificar se eh - comprimento
                while i < j and nums[j] == nums[j + 1]:
                    j -= 1
            elif(nums[i] + nums[j] > target):
                j -= 1
            else:
                i += 1
        return subset

    def threeSum(self, nums: List[int]) -> List[List[int]]:
        '''
        Sort array
        Para cada valor diferente, aplico o two sum

        '''
        nums.sort()
        response = []
        hash_nums = dict()
        print(nums)
        for idx in range(len(nums)-1):
            if idx > 0 and nums[idx] == nums[idx - 1]:
                continue
            twosum_subset = self.two_sum(nums, -nums[idx], idx+1)
            for subset in twosum_subset:
                subset.sort()
                # key = f'{subset[0]}-{subset[1]}-{subset[2]}'
                key = tuple(sorted(subset))
                if key not in hash_nums:
                    response.append(subset)
                    hash_nums[key] = 0
        return response
print(Solution().threeSum([-1,0,1,2,-1,-4]))