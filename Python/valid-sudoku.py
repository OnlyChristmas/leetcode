'''
Determine if a 9x9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

Each row must contain the digits 1-9 without repetition.
Each column must contain the digits 1-9 without repetition.
Each of the 9 3x3 sub-boxes of the grid must contain the digits 1-9 without repetition.

A partially filled sudoku which is valid.
The Sudoku board could be partially filled, where empty cells are filled with the character '.'.

Example 1:
Input:
[
  ["5","3",".",".","7",".",".",".","."],
  ["6",".",".","1","9","5",".",".","."],
  [".","9","8",".",".",".",".","6","."],
  ["8",".",".",".","6",".",".",".","3"],
  ["4",".",".","8",".","3",".",".","1"],
  ["7",".",".",".","2",".",".",".","6"],
  [".","6",".",".",".",".","2","8","."],
  [".",".",".","4","1","9",".",".","5"],
  [".",".",".",".","8",".",".","7","9"]
]
Output: true

Example 2:
Input:
[
  ["8","3",".",".","7",".",".",".","."],
  ["6",".",".","1","9","5",".",".","."],
  [".","9","8",".",".",".",".","6","."],
  ["8",".",".",".","6",".",".",".","3"],
  ["4",".",".","8",".","3",".",".","1"],
  ["7",".",".",".","2",".",".",".","6"],
  [".","6",".",".",".",".","2","8","."],
  [".",".",".","4","1","9",".",".","5"],
  [".",".",".",".","8",".",".","7","9"]
]
Output: false
Explanation: Same as Example 1, except with the 5 in the top left corner being
    modified to 8. Since there are two 8's in the top left 3x3 sub-box, it is invalid.

Note:
A Sudoku board (partially filled) could be valid but is not necessarily solvable.
Only the filled cells need to be validated according to the mentioned rules.
The given board contain only digits 1-9 and the character '.'.
The given board size is always 9x9.

'''



class Solution:
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        # 思路一：复杂的分条判断   76ms
#         for i in range(9):
#             if 9 - len(set(board[i])) != board[i].count(".") - 1:     # 条件一
#                 return False

#             new_list = []
#             for j in range(9):                                         # 条件二
#                 if board[j][i] != '.' and board[j][i] in new_list:
#                     return False
#                 if board[j][i] != '.' and board[j][i] not in new_list:
#                     new_list.append(board[j][i])


#         aa,bb = [0,3,6],[0,3,6]
#         for a in aa:                    # 条件三
#             for b in bb:
#                 new_list = []
#                 for i in range(a,a+3):
#                     for j in range(b,b+3):
#                         if board[i][j] != '.' and board[i][j] in new_list:
#                             return False
#                         if board[i][j] != '.' and board[i][j] not in new_list:
#                             new_list.append(board[i][j])

#         return True



        # 思路二： 只循环一次完成数据的分类，用存储空间来换取算法的效率（借鉴）。

#         dic_row = [{},{},{},{},{},{},{},{},{}]            # 每行的元素以一个字典储存，key是数字，value统一为1.
#         dic_col = [{},{},{},{},{},{},{},{},{}]
#         dic_box = [{},{},{},{},{},{},{},{},{}]

#         for i in range(len(board)):
#             for j in range(len(board)):
#                 num = board[i][j]
#                 if num == ".":
#                     continue
#                 if num not in dic_row[i] and num not in dic_col[j] and num not in dic_box[3*(i//3)+(j//3)]:
#                     dic_row[i][num] = 1
#                     dic_col[j][num] = 1
#                     dic_box[3*(i//3)+(j//3)][num] = 1       # 利用地板除，向下取余。巧妙地将矩阵划分为九块
#                 else:
#                     return False

#         return True




        # 思路三： 思路二的另一种实现方式。代码更为简洁
        Cell = [[] for i in range(9)]                   # 没有必要用dict,我们只某个数字关心有没有出现过
        Col =  [[] for i in range(9)]
        Row =  [[] for i in range(9)]

        for i,row in enumerate(board):                  # 将一个可遍历的数据对象(如列表、元组或字符串)组合为一个索引序列，同时列出数据和数据下标，一般用在 for 循环当中
            for j,num in enumerate(row):
                if num != '.':
                    k = (i//3)*3 + j//3
                    if num in Row[i] + Col[j] + Cell[k]:    # list的骚操作,将三个list顺序的拼接
                        return False
                    Row[i].append(num)
                    Col[j].append(num)
                    Cell[k].append(num)

        return True

