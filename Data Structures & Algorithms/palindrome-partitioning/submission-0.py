class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []

        def dfs(i, substring):
            if i >= len(s):
                res.append(substring.copy())
                return

            for j in range(i, len(s)):
                if isPalindrome(s, i, j):
                    substring.append(s[i : j + 1])
                    dfs(j + 1, substring)
                    substring.pop()

        def isPalindrome(s: str, l, r):
            while l < r:
                if s[l] != s[r]:
                    return False
                l += 1
                r -= 1
            return True

        dfs(0, [])
        return res