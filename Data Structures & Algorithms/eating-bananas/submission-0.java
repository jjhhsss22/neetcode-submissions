class Solution {
    public int minEatingSpeed(int[] piles, int h) {
        int l = 0;
        int r = Arrays.stream(piles).max().getAsInt();
        int k = r;

        while (l <= r) {
            int mid = (l + r) / 2;

            double time = 0;

            for (int pile : piles) {
                time += Math.ceil((double) pile / mid);
            }

            if (time <= h) {
                k = mid;
                r = mid - 1;
            } else {
                l = mid + 1;
            }
        }
        
        return k;
    }
}
