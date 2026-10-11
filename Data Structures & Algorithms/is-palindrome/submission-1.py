class Solution:
    def isPalindrome(self, s: str) -> bool:
        Lpointer = 0
        Rpointer = len(s) - 1

        while Lpointer < Rpointer:
            while not s[Lpointer].isalnum() and Lpointer < Rpointer:
                Lpointer += 1
            while not s[Rpointer].isalnum() and Rpointer > Lpointer:
                Rpointer -= 1

            if s[Lpointer].lower() != s[Rpointer].lower():
                return False

            Lpointer += 1
            Rpointer -= 1

        return True