class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        List<List<String>> result = new ArrayList<>();


        for (String text : strs) {
            List<String> anagram = new ArrayList<>();

            char[] checkList = text.toCharArray();
            Arrays.sort(checkList);


            for (String text2 : strs) {

                char[] tempCheckList = text2.toCharArray();
                Arrays.sort(tempCheckList);

                if (Arrays.equals(checkList, tempCheckList)) {
                    anagram.add(text2);
                }
            }

            if (!result.contains(anagram)) {
                result.add(anagram);
            }
        }
        
        return result;
    }
}
