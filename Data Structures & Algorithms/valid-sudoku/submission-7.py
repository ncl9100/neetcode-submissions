class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        dict = {}
        #check rows
        for i in range(len(board)):
            for j in range(len(board)):
                if board[i][j] in dict and board[i][j]!='.':
                    return False
                dict[board[i][j]] = 1
            dict = {}
        
        #check columns
        for i in range(len(board)):
            for j in range(len(board)):
                if board[j][i] in dict and board[j][i]!='.':
                    return False
                dict[board[j][i]] = 1
            dict = {}
        
        #check sub-boxes
        for i in range(0, len(board)):
            dict[i] = set()
        for i in range(len(board)):
            for j in range(len(board[0])):
                sub_box = (i//3)*3 + j//3
                if board[i][j] in dict[sub_box] and board[i][j]!='.':
                    return False
                dict[sub_box].add(board[i][j])

        return True

     


        