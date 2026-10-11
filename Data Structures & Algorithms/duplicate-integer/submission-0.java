

class Solution {
    public boolean hasDuplicate(int[] nums) {
        
        ArrayList<Integer> temp = new ArrayList<>();

        for (int num : nums) {
            if (!temp.contains(num)) {
                temp.add(num);
            } else {
                return true;
            }
        }

        return false;


    }
}