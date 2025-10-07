from typing import List
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        '''
        Objetivo: Sair do topo esquerdo ao fundo direito minimizando o tempo
        Perceba que novamente vem no topico de maximo ou minimo, oque já precisa me remeter a
        1. Algoritmo guloso: Nesse caso não faz sentido, porque pode ser que uma escolha boa proxima não seja uma boa local.
        2. Programação dinamica.
        
        '''

        dp = grid.copy()
        for idx_row in range(len(grid)):
            for idx_col in range(len(grid[0])):
                if idx_row > 0 and idx_col > 0:
                    dp[idx_row][idx_col] += min(dp[idx_row - 1][idx_col], dp[idx_row][idx_col - 1])
                elif idx_row > 0:
                    dp[idx_row][idx_col] += dp[idx_row - 1][idx_col]
                elif idx_col > 0:
                    dp[idx_row][idx_col] += dp[idx_row][idx_col - 1]
        return dp[-1][-1]
print(Solution().minPathSum(grid = [[1,2,3],[4,5,6]]))