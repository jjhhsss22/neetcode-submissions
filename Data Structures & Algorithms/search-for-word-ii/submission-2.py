class TrieNode:
    def __init__(self):
        self.children = {}
        self.end = False

    def insert(self, word):
        node = self

        for c in word:
            if c not in node.children:
                node.children[c] = TrieNode()
            node = node.children[c]
        node.end = True

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        ROWS, COLS = len(board), len(board[0])

        root = TrieNode()
        for word in words:
            root.insert(word)

        res = set()

        def dfs(node, r, c, visited, word):
            if (r < 0 or r >= ROWS or c < 0 or c >= COLS or
                (r, c) in visited or
                board[r][c] not in node.children):
                return

            visited.add((r, c))
            word += board[r][c]
            node = node.children[board[r][c]]

            if node.end:
                res.add(word)

            dfs(node, r + 1, c, visited, word)
            dfs(node, r - 1, c, visited, word)
            dfs(node, r, c + 1, visited, word)
            dfs(node, r, c - 1, visited, word)

            visited.remove((r, c))

        for r in range(ROWS):
            for c in range(COLS):
                dfs(root, r, c, set(), "")

        return list(res)