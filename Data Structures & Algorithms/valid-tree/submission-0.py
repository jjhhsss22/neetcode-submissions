class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        connections = [[] for _ in range(n)]

        for edge1, edge2 in edges:
            connections[edge1].append(edge2)
            connections[edge2].append(edge1)

        print (connections)

        visiting = set()
        clear = set()

        def dfs(node, prev):
            if node in visiting:
                return False
            if node in clear:
                return True

            visiting.add(node)

            for edge in connections[node]:
                if edge != prev:
                    if not dfs(edge, node):
                        return False

            visiting.remove(node)
            clear.add(node)

            return True

        return dfs(0, -1) and len(clear) == n