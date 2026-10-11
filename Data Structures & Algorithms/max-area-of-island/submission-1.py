class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROW, COL = len(grid), len(grid[0])

        def dfs(i, j):
            if i < 0 or i >= ROW or j < 0 or j >= COL or grid[i][j] != 1:
                return

            grid[i][j] = 0
            self.area += 1

            dfs(i - 1, j)
            dfs(i + 1, j)
            dfs(i, j - 1)
            dfs(i, j + 1)

        maxArea = 0

        for i in range(ROW):
            for j in range(COL):
                if grid[i][j] == 1:
                    self.area = 0
                    dfs(i, j)
                    maxArea = max(maxArea, self.area)

        return maxArea