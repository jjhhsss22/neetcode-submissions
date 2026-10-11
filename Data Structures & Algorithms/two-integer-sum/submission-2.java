class Solution {
    public int[] twoSum(int[] nums, int target) {
        
        int[] result = new int[2];

        for (int i = 0; i < nums.length; i++) {

            for (int j = 0; j < nums.length; j++) {
                if (i == j) {
                    continue;
                }
                int total = nums[i] + nums[j];

                if (total == target) {
                    result[0] = i;
                    result[1] = j;

                    Arrays.sort(result);

                    return result;
                }
            }
        }

        return null;

    }
}
