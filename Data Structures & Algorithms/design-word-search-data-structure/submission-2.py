class TrieNode:
    def __init__(self):
        self.children = {}
        self.end = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        node = self.root

        for c in word:
            if c not in node.children:
                node.children[c] = TrieNode()
            node = node.children[c]

        node.end = True

    def search(self, word: str) -> bool:

        def dfs(node, i):
            if i == len(word):
                return node.end

            if word[i] not in node.children and word[i] != ".":
                return False

            if word[i] == ".":
                for c in node.children:
                    if dfs(node.children[c], i + 1):
                        return True
                return False
            else:
                return dfs(node.children[word[i]], i + 1)

        return dfs(self.root, 0)
        
