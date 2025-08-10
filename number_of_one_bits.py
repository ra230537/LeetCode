class Solution:
    def hammingWeight(self, n: int) -> int:
        '''
        Eu diria que tem alguma coisa a ver com algo binário, 
        Daria para fazer aquele algoritmo de divisões sucessivas
        '''
        count = 0
        while (n > 0):
            rest = n % 2
            count += rest
            n-=rest
            n = n // 2
        return count
    
print(Solution().hammingWeight(2147483645))