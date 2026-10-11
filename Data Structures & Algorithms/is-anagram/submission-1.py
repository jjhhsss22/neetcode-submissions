class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        count = dict()

        for char in s:
            if char in count.keys():
                count[char] = count[char] + 1
            else:
                count[char] = 1

        for char in t:
            if char in count.keys():
                if count[char] > 1:
                    count[char] = count[char] - 1
                else:
                    del count[char]
            else:
                return False

        return True