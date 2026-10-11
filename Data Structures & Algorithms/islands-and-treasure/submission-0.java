class Solution {
    public void islandsAndTreasure(int[][] grid) {
        int INF = 2147483647;
        int ROW = grid.length;
        int COL = grid[0].length;

        Queue<int []> q = new LinkedList<>();

        for (int i = 0; i < ROW; i++) {
            for (int j = 0; j < COL; j++) {
                if (grid[i][j] == 0) {
                    q.add(new int []{ i, j });
                }
            }
        }

        int distance = 0;
        int[][] dirs = {{1,0}, {-1,0}, {0,1}, {0,-1}};

        while (!q.isEmpty()) {
            int [] pair = q.poll();
            int r = pair[0];
            int c = pair[1];

            for (int[] dir : dirs) {
                int nr = r + dir[0];
                int nc = c + dir[1];

                if (nr >= 0 && nr < ROW && nc >= 0 && nc < COL && grid[nr][nc] == INF) {
                    grid[nr][nc] = grid[r][c] + 1;
                    q.add(new int[] {nr, nc});
                }
            }
        }
    }
}
