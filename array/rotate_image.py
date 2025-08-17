

class Solution:
    def translate(self, matrix, m, n):
        for i in range(m):
            for j in range(i, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        return matrix
    def reverse(self, matrix,m, n):
        for i in range(m):
            for j in range(n//2):
                matrix[i][j], matrix[i][n-j-1] = matrix[i][n-1-j], matrix[i][j]
        return matrix
    def rotate(self, matrix: list[list[int]]) -> None:
        n = len(matrix)
        m = len(matrix[0])
        matrix = self.translate(matrix, m, n)
        matrix = self.reverse(matrix, m, n)
        return matrix
    def print_matrix(self, matrix):
        for i in range(len(matrix)):
            print(matrix[i])

matrix = Solution().rotate(matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]])
Solution().print_matrix(matrix)