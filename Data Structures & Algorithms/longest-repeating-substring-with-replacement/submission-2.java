class Solution {
    public int characterReplacement(String s, int k) {
        HashMap<Character, Integer> hashMap = new HashMap();

        int l = 0;
        int max = 0;
        int res = 0;

        for (int r = 0; r < s.length(); r++) {
            char c = s.charAt(r);

            hashMap.put(c, hashMap.getOrDefault(c, 0) + 1);

            max = Integer.max(max, hashMap.get(c));

            while (r - l - max + 1 > k) {
                char x = s.charAt(l);

                if (hashMap.get(x) == 1) {
                    hashMap.remove(x);
                } else hashMap.put(x, hashMap.get(x) - 1);
                
                l++;
            }
            
            res = Integer.max(res, r - l + 1);

        }
        
        return res;
    }
}
