class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList or beginWord == endWord:
            return 0

        neighbours = collections.defaultdict(list)

        for word in wordList:
            for i in range(len(word)):
                branch = word[:i] + "*" + word[i + 1:]
                neighbours[branch].append(word)

        queue = collections.deque([beginWord])

        visited = set()
        visited.add(beginWord)
        res = 1

        while queue:
            for _ in range(len(queue)):
                word = queue.popleft()

                if word == endWord:
                    return res

                for i in range(len(word)):
                    branch = word[:i] + "*" + word[i + 1:]

                    for nei in neighbours[branch]:
                        if nei not in visited:
                            queue.append(nei)
                            visited.add(nei)
                            
            res += 1
            
        return 0