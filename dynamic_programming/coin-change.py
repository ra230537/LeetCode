from typing import List
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0
        # Quantidade de moedas necessárias para chegar no valor i
        # Quando não houver moedas, que deem pra chegar no valor i -> deixamos como -1
        dp = [-1 for _ in range(amount + 1)]
        for value in range(amount + 1):
            for coin in coins:
                if coin > value:
                    continue
                elif coin == value:
                    dp[value] = 1
                # Preciso verificar se o valor que eu to querendo colocar é valido
                elif coin < value and dp[value - coin] > 0:
                    # Caso básico, basta preencher
                    if dp[value] == -1:
                        dp[value] = 1 + dp[value - coin]
                    # Caso haja valor, temos que ver qual o melhor valor
                    else:
                        dp[value] = min(dp[value], dp[value - coin] + 1)
        return dp[-1]
print(Solution().coinChange(coins = [1,2,5], amount = 11))