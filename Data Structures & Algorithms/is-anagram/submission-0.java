class Solution {
    public boolean isAnagram(String s, String t) {
        char[] sList;
        char[] tList;

        sList = s.toLowerCase().toCharArray();
        tList = t.toLowerCase().toCharArray();

        Arrays.sort(sList);
        Arrays.sort(tList);

        return Arrays.equals(sList, tList);
    }
}
