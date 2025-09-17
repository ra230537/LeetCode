from typing import List
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        '''
        É fácil ver que podemos usar programação dinamica para construir a resposta já que para um quadrado de posição i, j
        O numero de formas de chegar nessa posição é a quantidade de formas de chegar na posição (dp(i-1, j) + 1) + (dp(i, j - 1) + 1)
        '''
        dp = [[0 for _ in range(len(obstacleGrid[0]))] for _ in range(len(obstacleGrid))]
        for i in range(len(obstacleGrid)):
            for j in range(len(obstacleGrid[0])):
                if obstacleGrid[i][j] == 1:
                    continue
                if i > 0 and j > 0:
                    if obstacleGrid[i-1][j] == 0 and obstacleGrid[i][j - 1] == 0:
                        dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
                    elif obstacleGrid[i][j - 1] == 0:
                        dp[i][j] = dp[i][j - 1]
                    elif obstacleGrid[i - 1][j] == 0:
                        dp[i][j] = dp[i - 1][j]
                elif i > 0:
                    if obstacleGrid[i - 1][j] == 0:
                        dp[i][j] = dp[i - 1][j]
                elif j > 0:
                    if obstacleGrid[i][j - 1] == 0:
                        dp[i][j] = dp[i][j - 1]
                else:
                    dp[i][j] = 1
        print(dp)
        return dp[-1][-1]
print(Solution().uniquePathsWithObstacles(obstacleGrid = [[0,0],[0,1]]))