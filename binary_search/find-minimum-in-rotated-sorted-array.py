from typing import List
class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums)-1
        mid = (left+right)//2
        min_value = 99999
        while left <= right:
            # Se o lado direito for maior que o meio => Eu estou na parte não rotacionada,
            # Caso contrário, o lado direito sempre deveria ser menor que o meio já que foi rotacionado
            min_value = min(min_value, nums[mid])
            if (nums[mid] < nums[right]):
                right = mid - 1
            # Se o lado direito for menor que o meio => Eu estou na parte rotacionada
            elif (nums[mid] > nums[right]):
                left = mid + 1
            else:
                break
            mid = (left+right)//2
        print(min_value)
        return min_value
assert Solution().findMin(nums = [4,5,6,7,8,9,10,11,12,13,14,-1,0,1,2,3]) == -1
assert Solution().findMin(nums = [4,5,6,7,0,1,2]) == 0
assert Solution().findMin(nums = [1]) == 1
assert Solution().findMin(nums = [1,2, 3,4,5,6]) == 1
assert Solution().findMin(nums = [7,8,1,2, 3,4,5,6]) == 1
'''
Duas possibilidades:
Possibilidade numero 1:
O lado esquerdo é maior que eu: Se isso acontecer, eu estou na parte que não foi rotacionada (A direita) e eu não quero ir mais a direita
Então O meu teto fica sendo mid - 1

O lado direito é menor que eu: Se isso acontecer, eu estou na parte que  foi rotacionada (A esquerda) e eu não quero ir mais a esquerda
Então O meu piso fica sendo mid + 1

Possibilidade numero 2:
O lado esquerdo é menor do que eu: Se isso acontecer, pode ser ok. Mas ai eu vou tá em qualquer um dos lados

3 possibilidades
Eu to do lado esquerdo e a esquerda tá do meu lado  -> Eu não quero estar desse lado, então left = mid + 1
Eu to do lado direito e a esquerda tá do meu lado -> Nesse caso, a resposta seria nums[left], mas eu também poderia fazer right = mid - 1
Eu to do lado direito e a esquerda ta do lado esquerdo -> right = mid - 1

Chão = mid + 1
'''