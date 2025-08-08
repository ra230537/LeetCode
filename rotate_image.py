'''
j <- i
i <- N - j
Para cada camada 0 -> n//2
para cada posicao_inicial (0 -> n-1)
Para cada 4 trocas
'''


class Solution:
    def new_position(self, i, j, n):
        if (i < n//2):
            new_j = n - i - 1
        else:
            pass
        return (j, new_j)
    def rotate(self, matrix: list[list[int]]) -> None:
        n = len(matrix)
        for layer in range(n//2):
            j = layer
            for start_position in range(n-1):
                i = layer + start_position
                current = matrix[i][j]
                for _ in range(4):
                    new_i, new_j = self.new_position(i, j, n)
                    print(new_i, new_j)
                    temp = matrix[new_i][new_j]
                    matrix[new_i][new_j] = current
                    current = temp
                    i, j = new_i, new_j
        return matrix
    def print_matrix(self, matrix):
        for i in range(len(matrix)):
            print(matrix[i])
        """
        Do not return anything, modify matrix in-place instead.
        """

matrix = Solution().rotate(matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]])
Solution().print_matrix(matrix)