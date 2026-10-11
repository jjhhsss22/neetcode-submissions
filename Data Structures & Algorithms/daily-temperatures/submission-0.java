class Solution {
    public int[] dailyTemperatures(int[] temperatures) {
        int[] res = new int[temperatures.length];
        Stack<Integer> st = new Stack<>();

        for (int i = 0; i < temperatures.length; i++) {

            while (!st.empty() && temperatures[st.peek()] < temperatures[i]) {
                res[st.peek()] = i - st.peek();
                st.pop();
            }

            st.push(i);
        }

        for (Integer x : st) {
            res[x] = 0;
        }
        
        return res;
    }
}
