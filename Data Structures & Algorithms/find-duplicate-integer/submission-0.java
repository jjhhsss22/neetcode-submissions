class Solution {
    public int findDuplicate(int[] nums) {
        HashSet<Integer> hashSet = new HashSet<>();

        for (int num : nums) {
            if (hashSet.contains(num)) {
                return num;
            } else {
                hashSet.add(num);
            }
        }

    return -1;
    }
}
