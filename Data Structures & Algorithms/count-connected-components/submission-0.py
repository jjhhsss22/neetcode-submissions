class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        connections = [[] for _ in range(n)]

        for edge1, edge2 in edges:
            connections[edge1].append(edge2)
            connections[edge2].append(edge1)

        visited = [False] * n

        def dfs(node):
            visited[node] = True

            for edge in connections[node]:
                if not visited[edge]:
                    dfs(edge)

        components = 0

        for i in range(n):
            if not visited[i]: 
                components += 1
                dfs(i)

        return components