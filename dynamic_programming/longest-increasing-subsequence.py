from typing import List
'''
TODO: Anotar essa solução
Essa questão tem uma solução que aparentemente é manjada:
from typing import List
import bisect

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        sub = []  # will store the increasing subsequence (not necessarily valid LIS but correct length)
        for num in nums:
            # find position to replace in sub
            pos = bisect.bisect_left(sub, num)
            if pos == len(sub):
                sub.append(num)   # extend
            else:
                sub[pos] = num    # replace smaller candidate
        return len(sub)

Isso é feito em O(nlog(n))
Usando esse modulo que faz uma inserção em tempo O(log(n))
Basicamente, a gente tem uma lista que vai conter uma subsequencia com o tamanho correto.
Dai se o numero for adicionado no final quer dizer que achamos um numero maior para a subsequencia,então ela pode crescer
Se o numero for adicionado no meio, substitui por um candidato menor (o bissect_left vai dar a posição do item que fica a esquerda do target)
Example: arr = [3, 4, 5, 1, 2, 3, 4] Let's see why keeping 1 (the smallest value) helps:

We use binary search to find the position where new element is to be inserted.

First three elements: buckets = [3, 4, 5]
arr[3] = 1 buckets = [1, 4, 5]  // 1 replaces 3
arr[4] = 2 buckets = [1, 2, 5]  // 2 replaces 4 as it's smaller
arr[5] = 3 buckets = [1, 2, 3]  // 3 replaces 5
arr[6] = 4 buckets = [1, 2, 3, 4]  // 4 is appended as it's larger
'''
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # Guarda a melhor sequencia de numeros
        # A melhor sequencia para um numero em i, pode ser montada pela melhor sequencia dp[k] k > 0 and k<i 0 tq nums[k] < nums[i]
        dp = [0 for _ in range(len(nums))]
        dp[0] = 1
        for i in range(1, len(nums)):
            best_dp = 0
            for k in range(i):
                if (nums[k] < nums[i]):
                    best_dp = max(best_dp, dp[k])
            dp[i] = best_dp + 1
        return max(dp)
assert Solution().lengthOfLIS(nums = [10,9,2,5,3,7,101,18]) == 4
assert Solution().lengthOfLIS(nums = [0,1,0,3,2,3]) == 4
assert Solution().lengthOfLIS(nums = [7,7,7,7,7,7,7]) == 1