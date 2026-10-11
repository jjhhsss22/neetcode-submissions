class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        return self.check_row(board) and self.check_column(board) and self.check_box(board)

    def check_row(self, board):
        for i in range(len(board)):
            hash_set = set()

            for j in range(len(board[i])):
                if board[i][j] != ".":
                    if board[i][j] in hash_set:
                        return False

                    hash_set.add(board[i][j])

        return True

    def check_column(self, board):

        for i in range(len(board)):
            hash_set = set()

            for j in range(len(board[i])):
                if board[j][i] != ".":
                    if board[j][i] in hash_set:
                        return False

                    hash_set.add(board[j][i])

        return True

    def check_box(self, board):

        for i in range(0, len(board), 3):
            for j in range(0, len(board[i]), 3):

                hash_set = set()

                for a in range(3):
                    for b in range(3):

                        row = j + b
                        col = i + a

                        if board[row][col] != ".":
                            if board[row][col] in hash_set:
                                return False
                            
                            hash_set.add(board[row][col])

        return True
            