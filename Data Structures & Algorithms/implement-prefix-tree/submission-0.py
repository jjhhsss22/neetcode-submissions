class PrefixTreeNode:
    def __init__(self):
        self.children = {}
        self.end = False

class PrefixTree:
    def __init__(self):
        self.root = PrefixTreeNode()

    def insert(self, word: str) -> None:
        node = self.root

        for c in word:
            if c not in node.children:
                node.children[c] = PrefixTreeNode()
            node = node.children[c]
        node.end = True

    def search(self, word: str) -> bool:
        node = self.root

        for c in word:
            if c not in node.children:
                return False
            node = node.children[c]

        if node.end:
            return True
        return False

    def startsWith(self, prefix: str) -> bool:
        node = self.root
        
        for c in prefix:
            if c not in node.children:
                return False
            node = node.children[c]
        
        return True
        
        