class Solution {
    public int orangesRotting(int[][] grid) {
        int ROW = grid.length;
        int COL = grid[0].length;
        int fresh = 0;

        Queue<int []> q = new LinkedList<>();

        for (int i = 0; i < ROW; i++) {
            for (int j = 0; j < COL; j++) {
                if (grid[i][j] == 1) {
                    fresh++;
                }

                if (grid[i][j] == 2) {
                    q.add(new int []{ i, j });
                }
            }
        }

        int[][] dirs = {{1,0}, {-1,0}, {0,1}, {0,-1}};
        int time = 0;

        while (!q.isEmpty() && fresh > 0) {
            int length = q.size();
            for (int i = 0; i < length; i++) {
                int[] pair = q.poll();
                int r = pair[0];
                int c = pair[1];

                for (int[] dir : dirs) {
                    int nr = r + dir[0];
                    int nc = c + dir[1];

                    if (nr >= 0 && nr < ROW && nc >= 0 && nc < COL && grid[nr][nc] == 1) {
                        grid[nr][nc] = 2;
                        q.add(new int[]{nr, nc});
                        fresh--;
                    }
                }
            }
            time++;
        }

        return (fresh == 0) ? time : -1;
    }
}
