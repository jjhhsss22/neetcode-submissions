class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res= []
        board = [["."] * n for _ in range(n)]

        def backtrack(r, board):
            if r == n:
                valid_board = []

                for row in board:
                    valid_board.append("".join(row))

                res.append(valid_board)

            for c in range(n):
                if checkQ(board, r, c):
                    board[r][c] = "Q"
                    backtrack(r + 1, board)
                    board[r][c] = "."
            
        def checkQ(board, r, c):
            row = r - 1

            while row >= 0:
                if board[row][c] == "Q":
                    return False
                row -= 1

            row = r - 1
            col = c - 1

            while col >= 0 and row >= 0:
                if board[row][col] == "Q":
                    return False
                row -= 1
                col -= 1

            row = r - 1
            col = c + 1

            while col <= len(board) - 1 and row >= 0:
                if board[row][col] == "Q":
                    return False
                row -= 1
                col += 1

            return True

        backtrack(0, board)
        return res