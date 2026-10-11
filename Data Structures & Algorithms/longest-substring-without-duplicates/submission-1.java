class Solution {
    public int lengthOfLongestSubstring(String s) {
        if (s.isEmpty()) return 0;

        HashMap<Character, Integer> hashMap = new HashMap<>();

        int l = 0, maximum = 0;

        for (int r = 0; r < s.length(); r++) {
            char rChar = s.charAt(r);

            hashMap.put(rChar, hashMap.getOrDefault(rChar, 0) + 1);

            while (hashMap.get(rChar) > 1) {
                char x = s.charAt(l);

                hashMap.put(x, hashMap.getOrDefault(x, 0) - 1);

                if (hashMap.get(x) == 0) {
                    hashMap.remove(x);
                }

                l++;
            }

            maximum = Integer.max(maximum, hashMap.size());
        }

        return maximum;
        
    }
}