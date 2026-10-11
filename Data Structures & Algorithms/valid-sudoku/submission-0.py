class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        if self.checkRow(board) and self.checkCol(board) and self.checkSquare(board):
            return True
        else:
            return False

    def checkRow(self, board):
        for i in range(len(board)):
            seen = []
            for j in range(len(board[i])):
                if board[i][j] != ".":
                    if board[i][j] not in seen:
                        seen.append(board[i][j])
                    else:
                        return False

        return True

    def checkCol(self, board):
        for i in range(len(board)):
            seen = []
            for j in range(len(board[i])):
                if board[j][i] != ".":
                    if board[j][i] not in seen:
                        seen.append(board[j][i])
                    else:
                        return False

        return True

    def checkSquare(self, board):
        for i in range(len(board)):
            seen = []
            for j in range(len(board) // 3):
                for k in range(len(board[i]) // 3):
                    row = (i // 3) * 3 + j
                    col = (i % 3) * 3 + k

                    if board[row][col] != ".":
                        if board[row][col] not in seen:
                            seen.append(board[row][col])
                        else:
                            return False

        return True