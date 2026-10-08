class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        rows = {}      # similar to HashMap<Integer, Integer>
        columns = {}
        squares = {}

        # check rows
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] != '.':
                    parsed = int(board[i][j])
                    print(parsed)
                    if parsed in rows and rows[parsed] == i:
                        print("rows fail")
                        return False
                    rows[parsed] = i

        # check columns
        for i in range(len(board[0])):
            for j in range(len(board)):
                if board[j][i] != '.':
                    parsed = int(board[j][i])
                    if parsed in columns and columns[parsed] == i:
                        print("columns fail")
                        return False
                    columns[parsed] = i

        # check 3x3 squares
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] != '.':
                    square_index = (i // 3) * 3 + (j // 3)
                    parsed = int(board[i][j])
                    if parsed in squares and squares[parsed] == square_index:
                        print(parsed)
                        return False
                    squares[parsed] = square_index

        return True
