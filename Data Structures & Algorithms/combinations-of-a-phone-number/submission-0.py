class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res = []
        hash = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "qprs",
            "8": "tuv",
            "9": "wxyz",
        }

        def dfs(i, s):
            if i == len(digits):
                res.append(s)
                return
            
            for j in range(len(hash[digits[i]])):
                dfs(i + 1, s + hash[digits[i]][j])
        
        if digits:
            dfs(0, "")
        return res