from typing import List
# TODO ANOTAR A IDEIA DO K QUE ANDA
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        '''
        Tu vai ter um k que representa o proximo numero diferente deveria estar
        Tu vai ter um contador porque agora a gente só vai atualizar k quando o contador for maior que 1
        O valor na posição k deve ser atualizado sempre já que ele representa o novo vetor
        no pior dos casos, vamos atualizar o valor de k por ele mesmo
        '''
        k  = 1
        equal_count = 0
        for idx in range(1, len(nums)):
            nums[k] = nums[idx]
            if (nums[idx] == nums[idx-1]):
                equal_count +=1
                if (equal_count < 2):
                    k+=1
            else:
                k+=1
                equal_count = 0

        print(nums[:k])
        return k
print(Solution().removeDuplicates(nums = [0,0,1,1,1,1,2,3,3]))