class Solution {

    public String encode(List<String> strs) {
        StringBuilder plain = new StringBuilder();

        for (String word : strs) {
            plain.append(word.length()).append("#").append(word);
        }

        return plain.toString();
    }

    public List<String> decode(String str) {
         List<String> code = new ArrayList<>();

            int i = 0;

            while (i < str.length()) {
                int j = i;

                while (str.charAt(j) != '#') {
                    j++;
                }

                int wordLength = Integer.parseInt(str.substring(i, j));

                String word = str.substring(j + 1, j + 1 + wordLength);
                code.add(word);

                i = j + wordLength + 1;
            }
            
        return code;
    }
}
