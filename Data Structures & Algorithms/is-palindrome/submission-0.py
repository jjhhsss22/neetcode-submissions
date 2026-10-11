class Solution:
    def isPalindrome(self, s: str) -> bool:
        for letter in s:
            if not letter.isdigit() and not letter.isalpha():
                s = s.replace(letter, "")

        s = s.lower()

        for i in range(len(s) // 2):
            if s[i] != s[len(s) - i - 1]:
                return False

        return True