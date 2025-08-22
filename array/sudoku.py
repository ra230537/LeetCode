from typing import List
class Solution:
    def verify_row_repetition(self, board: List[List[str]]):
        for row in board:
            verify_list = [False for _ in range(9)]
            for column in row:
                if (column != '.'):
                    numerical_column = int(column)-1
                    if (numerical_column > 8 or numerical_column < 0):
                        return False
                    else:
                        # lista já foi marcada como verdadeiro, então repetido
                        if (verify_list[numerical_column]):
                            return False
                        else:
                            verify_list[numerical_column] = True
        return True
    def verify_column_repetition(self, board: List[List[str]]):
        m = len(board)
        n = len(board[0])
        for column_idx in range(n):
            verify_list = [False for _ in range(9)]
            for row_idx in range(m):
                if (board[row_idx][column_idx] != '.'):
                    numerical_column = int(board[row_idx][column_idx])-1
                    if (numerical_column > 8 or numerical_column < 0):
                        return False
                    else:
                        # lista já foi marcada como verdadeiro, então repetido
                        if (verify_list[numerical_column]):
                            return False
                        else:
                            verify_list[numerical_column] = True
        return True
    def box_repetition(self, board: List[List[str]]):
        rows_steps = [0, 3, 6]
        columns_steps = [0, 3, 6]
        for row_start in rows_steps:
            for column_start in columns_steps:
                verify_list = [False for _ in range(9)]
                for row_idx in range(row_start, row_start + 3):
                    for column_idx in range(column_start, column_start + 3):
                        if (board[row_idx][column_idx] != '.'):
                            cell = int(board[row_idx][column_idx])-1
                            if (cell > 8 or cell < 0):
                                return False
                            else:
                                # lista já foi marcada como verdadeiro, então repetido
                                if (verify_list[cell]):
                                    return False
                                else:
                                    verify_list[cell] = True
        return True
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        is_valid_column = self.verify_column_repetition(board)
        # print(is_valid_column)
        is_valid_row = self.verify_row_repetition(board)
        # print(is_valid_row)
        is_valid_box = self.box_repetition(board)
        # print(is_valid_box)
        return is_valid_column and is_valid_row and is_valid_box
    
print(Solution().isValidSudoku(board = 
[["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]))