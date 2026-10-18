class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = [[False] * len(grid[0]) for _ in range(len(grid))]
        ans = 0

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1' and not visited[i][j]:
                    self.dfs(grid, [i, j], visited)
                    ans += 1

        return ans
        

    def dfs(self, grid, current, visited):
        row, col = current

        if row < 0 or row > len(grid) - 1 or col < 0 or col > len(grid[0]) - 1 or visited[row][col] or grid[row][col] == '0':
            return None

        visited[row][col] = True

        self.dfs(grid, [row - 1, col], visited)
        self.dfs(grid, [row + 1, col], visited)
        self.dfs(grid, [row, col - 1], visited)
        self.dfs(grid, [row, col + 1], visited)
        