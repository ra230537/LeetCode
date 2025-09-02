from typing import List
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        start_i = 0
        end_i = len(matrix) - 1
        count = 0
        start_j = 0
        end_j = len(matrix[0]) - 1
        i = start_i
        j = start_j
        response = []
        x_direction = 1
        y_direction = 0
        # response.append(matrix[0][0])
        while start_i <= end_i and start_j <= end_j:
            count += 1
            response.append(matrix[i][j])
            # print(response)
            if x_direction == 1 and j == end_j:
                x_direction = 0
                y_direction = 1
                start_i += 1

            elif y_direction == 1 and i == end_i:
                x_direction = -1
                y_direction = 0
                end_j -= 1

            elif x_direction == -1 and j == start_j:
                x_direction = 0
                y_direction = -1
                end_i -= 1

            elif y_direction == -1 and i == start_i:
                x_direction = 1
                y_direction = 0
                start_j += 1

            i , j = i + y_direction, j + x_direction

        return response
    
print(Solution().spiralOrder(matrix = [[1,2,3],[4,5,6],[7,8,9]]))