# https://neetcode.io/problems/valid-sudoku

from collections import defaultdict
def i_j_to_quadrant(i, j):
    return (i // 3) * 3 + (j // 3)
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row = [defaultdict(int) for _ in range(9)]
        col = [defaultdict(int) for _ in range(9)]
        quadrant_dict = [defaultdict(int) for _ in range(9)]
        for i in range(0,9):
            for j in range(0,9):
                if board[i][j]!='.':
                    quadrant = i_j_to_quadrant(i,j)
                    if board[i][j] in quadrant_dict[quadrant] or board[i][j] in row[i] or board[i][j] in col[j]:
                        return False
                    row[i][board[i][j]] = 1
                    col[j][board[i][j]] = 1
                    quadrant_dict[quadrant][board[i][j]] = 1
        return True

# time complexity: O(n^2) --> O(9^2) --> O(1)
# space complexity: 3 * O(n^2) --> 3 * O(9^2) --> O(1)