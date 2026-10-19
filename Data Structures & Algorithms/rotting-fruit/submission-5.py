from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        queue = deque()
        fresh = 0
        fresh_rotten = 0
        minutes = -1
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 2:
                    queue.append([i, j])
                if grid[i][j] == 1:
                    fresh += 1

        if fresh == 0:
            return 0

        while len(queue) != 0:
            temp_queue = []
            temp_queue.extend(queue)
            queue.clear()
            minutes += 1

            while len(temp_queue) != 0:
                row, col = temp_queue.pop()

                for x, y in directions:
                    next_row = row + x
                    next_col = col + y

                    if next_row >= 0 and next_row <= len(grid) - 1 and next_col >= 0 and next_col <= len(grid[0]) - 1 and grid[next_row][next_col] == 1:
                        queue.append([next_row, next_col])
                        grid[next_row][next_col] = 2
                        fresh_rotten += 1

        if fresh_rotten != fresh:
            return -1
        return minutes