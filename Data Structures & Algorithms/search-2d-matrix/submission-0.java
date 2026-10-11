class Solution {
    public boolean searchMatrix(int[][] matrix, int target) {

        int rows = matrix.length;
        int cols = matrix[0].length;

        int l = 0, r = rows * cols - 1;

        while (l <= r) {
            int mid = (l + r) / 2;

            int midvalue = matrix[mid / cols][mid % cols];

            if (midvalue == target) {
                return true;
            } else if (midvalue > target) {
                r = mid - 1;
            } else {
                l = mid + 1;
            }
        }
        
        return false;

    }
}
