class Solution:
    def countPrimes(self, n: int) -> int:
        n = max(n, 2)
        prime_list = [True for _ in range(n)]
        prime_list[0] = prime_list [1] = False
        for i in range(2, int(n**0.5) + 1):
            for k in range(2 * i, n, i):
                prime_list[k] = False
        return sum(prime_list)
print(Solution().countPrimes(1))
'''
Só precisamos testar até a raiz quadrada porque se a gente não encontrou nenhuym numero que forma n até la, não vamos mais encontrar, se houvesse
precisaria antes ter um que fica antes de N, então se não vamos encontrar nenhum fator de N até lá, porque procurariamos?
'''