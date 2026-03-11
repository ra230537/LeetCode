from typing import List
from collections import deque
'''
Problema:
Temos uma lista de produtos
Vamos ter que retornar uma lista também
Para cada produto na lista, vamos precisar achar um desconto equivalente de forma que o desconto vai ser o primeiro prices[j]
j > i e prices[j] <= prices[i]
'''

class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        ans = []
        for i, price in enumerate(prices):
            ans.append(price)
            for j, discount in enumerate(prices):
                if j <= i:
                    continue
                if discount <= price:
                    ans[-1] = price - discount
                    break
                
        return ans
    
    '''
    TODO:Tem uma abordagem muito inteligente usando uma pilha monotonica que basicamente faz o seguinte:
    Se a pilha está vazia, coloca um elemento na pilha
    O proximo elemento a ser colocado na pilha vai verificar se ele é menor do que o ultimo elemento da pilha, se for, voce aplica o desconto
    ou seja, reduz o valor do ultimo elemento em um valor correspondente ao novo elemento e faz isso até não dar mais. Sempre que der, voce remove o elemento da pilha
    Pois ele já ganhou o desconto dele.
    A pilha precisa apenas guardar os indices que estão esperando desconto e não o valor em si.
    Sempre que fazemos essa operação adicionamos o novo elemento na pilha pois agora eh ele que está esperando desconto
    
    UTILIDADE: Utilize a Pilha Monotônica sempre que precisar encontrar, para cada elemento de uma lista, 
    o seu primeiro vizinho (à esquerda ou à direita) que seja maior ou menor que ele, 
    otimizando buscas que seriam quadráticas O(n^2) para tempo linear O(n) ao manter os candidatos em uma ordem de grandeza organizada dentro da pilha 
    '''
    
    def finalPricesv2(self, prices: List[int]) -> List[int]:
        # Guarda o indice dos preços que estão aguardando por desconto
        waiting_discount = deque()
        for i, current_price in enumerate(prices):
            # Verifica se o preço referente ao ultimo elemento da pilha eh maior que o preço atual
            # se for, tira ele da pilha e atualiza o valor no prices
            while waiting_discount and prices[waiting_discount[-1]] >= current_price:
                price_index = waiting_discount.pop()
                prices[price_index] -= current_price
            waiting_discount.append(i)
        return prices
print(Solution().finalPricesv2(prices = [10,1,1,6]))
