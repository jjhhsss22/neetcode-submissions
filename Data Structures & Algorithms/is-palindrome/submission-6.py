class Solution:
    def isPalindrome(self, s: str) -> bool:
        ss = [c.lower() for c in s if c.isalpha() or c.isdigit()]

        left = 0
        right = len(ss) - 1

        while left <= right:
            if ss[left] != ss[right]:
                return False

            left += 1
            right -= 1
        
        return True