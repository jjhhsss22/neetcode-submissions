class Solution {
    public int[] topKFrequent(int[] nums, int k) {
        List<Integer> result = new ArrayList<>();

        HashMap<Integer, Integer> hashMap = new HashMap<>();

        for (int num : nums) {
            if(!hashMap.containsKey(num)) {
                hashMap.put(num, 1);
            } else {
                hashMap.put(num, hashMap.get(num) + 1);
            }
        }

        List<Integer> keys = new ArrayList<>(hashMap.keySet());
        keys.sort((a, b) -> hashMap.get(b) - hashMap.get(a));

        for (int i = 0; i < k; i++) {
            result.add(keys.get(i));
        }

        int[] answer = new int[k];

        for (int i = 0; i < result.size(); i++) {
            answer[i] = result.get(i);
        }

        return answer;
    }
}
