class Solution:
    def climbStairs(self, n: int) -> int:
        '''Algoritmo simples, salva quantos passos leva para chegar num lugar,
        para o proximo andar voce pode chegar partindo do anterior + 1 ou do antepenultimo +2'''
        response = []
            
        for i in range(0, n):
            if (i == 0):
                response.append(1)
            elif(i==1):
                response.append(2)
            else:
                response.append(response[i-1]+response[i-2])
        return response[-1]
print(Solution().climbStairs(4))

