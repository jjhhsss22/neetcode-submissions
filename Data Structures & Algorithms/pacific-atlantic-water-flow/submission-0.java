class Solution {
    public List<List<Integer>> pacificAtlantic(int[][] heights) {
            int ROW = heights.length, COL = heights[0].length;

        boolean [][] pacific = new boolean[ROW][COL];
        boolean [][] atlantic = new boolean[ROW][COL];

        Queue<int []> pq = new LinkedList<>();
        Queue<int []> aq = new LinkedList<>();
        
        for (int i = 0; i < ROW; i++) {
            pq.add(new int[] {i, 0});
            pacific[i][0] = true;

            aq.add(new int[] {i, COL - 1});
            atlantic[i][COL - 1] = true;
        }

        for (int j = 0; j < COL; j++) {
            pq.add(new int[] {0, j});
            pacific[0][j] = true;

            aq.add(new int[] {ROW - 1, j});
            atlantic[ROW - 1][j] = true;
        }

        bfs(pq, pacific, heights);
        bfs(aq, atlantic, heights);

        List<List<Integer>> res = new ArrayList<>();

        for (int i = 0; i < ROW; i++) {
            for (int j = 0; j < COL; j++) {
                if (pacific[i][j] && atlantic[i][j]) {
                    res.add(Arrays.asList(i, j));
                }
            }
        }
        
        return res;
    }

    private void bfs(Queue<int []> q, boolean[][] table, int[][] heights) {
        int ROW = heights.length, COL = heights[0].length;
        int[][] dirs = {{1, 0}, {-1, 0}, {0, 1}, {0, -1}};

        while (!q.isEmpty()) {
            int[] coord = q.poll();
            int r = coord[0], c = coord[1];

            for (int[] dir : dirs) {
                int nr = r + dir[0];
                int nc = c + dir[1];

                if (nr >= 0 && nr < ROW && nc >= 0 && nc < COL && !table[nr][nc] && heights[nr][nc] >= heights[r][c]) {
                    table[nr][nc] = true;
                    q.add(new int[] {nr, nc});
                }
            }
        }
    }    

}
