class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        '''
        Como eu so posso fazer uma compra e uma venda, então eu preciso saber o menor valor possivel pra eu ter o maior delta
        e a resposta eu vou armazenando
            Buscar o lucro maximo -> inicia como 0
            ter uma variavel de minimo
            para cada item
                se o valor for menor que a variavel de minimo atualiza.
                item atual - variavel de minimo
                se o valor for maior que o lucro maximo, atualiza
        '''
        max_profit = 0
        min_price = prices[0]
        for price in prices:
            min_price = min(min_price, price)
            max_profit = max(price - min_price, max_profit)
        return max_profit

      
print(Solution().maxProfit(prices = [7,6,4,3,1]))