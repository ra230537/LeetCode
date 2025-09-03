class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        matrix = [['' for _ in range(len(s))] for _ in range(numRows)]
        i = 0
        j = 0
        is_direction_down = True
        for idx in range(len(s)):
            matrix[i][j] = s[idx]
            if (i == 0):
                is_direction_down = True
            elif(i == numRows - 1):
                is_direction_down = False
            if (is_direction_down):
                i += 1
            else:
                i -= 1
                j += 1
        response = ''
        for idx_i in range(len(matrix)):
            for idx_j in range(len(matrix[0])):
                if (matrix[idx_i][idx_j] != ''):
                    response+=matrix[idx_i][idx_j]
        return response
    
print(Solution().convert(s = "AB", numRows = 1))