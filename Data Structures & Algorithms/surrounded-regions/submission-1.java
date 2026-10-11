class Solution {
    public void solve(char[][] board) {
        int ROW = board.length, COL = board[0].length;
        Queue<int[]> q = new LinkedList<>();

        for (int i = 0; i < ROW; i++) {
            if (board[i][0] == 'O') q.add(new int[]{i, 0});
            if (board[i][COL - 1] == 'O') q.add(new int[]{i, COL - 1});
        }

        for (int j = 0; j < COL; j++) {
            if (board[0][j] == 'O') q.add(new int[] {0, j});
            if (board[ROW - 1][j] == 'O') q.add(new int[] {ROW - 1, j});
        }

        int[][] dirs = {{1, 0}, {-1, 0}, {0, 1}, {0, -1}};
        boolean[][] visited = new boolean[ROW][COL];

        while (!q.isEmpty()) {
            int[] coord = q.poll();
            int r = coord[0], c = coord[1];

            visited[r][c] = true;

            for (int[] dir : dirs) {
                int nr = r + dir[0];
                int nc = c + dir[1];

                if (nr >= 0 && nr < ROW && nc >= 0 && nc < COL && board[nr][nc] == 'O' && !visited[nr][nc]) {
                    q.add(new int[] {nr, nc});
                }
            }
        }

        for (int i = 0; i < ROW; i++) {
            for (int j = 0; j < COL; j++) {
                char c = board[i][j];
                if (c == 'O' && !visited[i][j]) {
                    board[i][j] = 'X';
                }
            }
        }
    }
}
