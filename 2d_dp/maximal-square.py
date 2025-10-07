from typing import List
class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        m = len(matrix)
        n = len(matrix[0])
        # Tamanho maximo do quadrado em que o elemento é uma borda inferior direita
        dp = [[0 for _ in range(n)] for _ in range(m)]
        response = 0
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == '1':
                    matrix[i][j] = 1
                    dp[i][j] = 1
                else:
                    matrix[i][j] = 0
        if (m == 1):
            return max(matrix[0])
        if (n == 1):
            max_value = 0
            for i in range(m):
                max_value = max(max_value, matrix[i][0])
            return max_value
        dp[0][0] = matrix[0][0]
        for i in range(1, m):
            dp[i][0] = matrix[i][0]
        for j in range(1, n):
            dp[0][j] = matrix[0][j]
        for i in range(1, m):
            for j in range(1, n):
                left = dp[i][j-1]
                right = dp[i - 1][j]
                transversal = dp[i-1][j-1]
                # Todos forem um ou mais
                if(matrix[i][j] == 0):
                    continue
                if (left and right and transversal):
                    dp[i][j] = min(left, right, transversal) + 1
                # Algum deles for 0
                else:
                    dp[i][j] = 1
        # for i in range(m):
        #     print(matrix[i])
        # print('------------------------------------')
        # for i in range(m):
        #     print(dp[i])
        response = 0
        for i in range(m):
            for j in range(n):
                response = max(response, dp[i][j])
        return response ** 2
                
      
print(Solution().maximalSquare(matrix = [["1","1","1","1","1"],["1","1","1","1","1"],["0","0","0","0","0"],["1","1","1","1","1"],["1","1","1","1","1"]]))



assert Solution().maximalSquare(matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]) == 4
assert Solution().maximalSquare(matrix = [["0","1"],["1","0"]]) == 1
assert Solution().maximalSquare(matrix = [["1","0"],["1","0"]]) == 1
assert Solution().maximalSquare(matrix = [["0"]]) == 0
assert Solution().maximalSquare(matrix = [["0","0"],["0","0"]]) == 0
assert Solution().maximalSquare(matrix = [["1","1","1","1","1"],["1","1","1","1","1"],["0","0","0","0","0"],["1","1","1","1","1"],["1","1","1","1","1"]]) == 4