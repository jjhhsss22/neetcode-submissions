class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        counter = dict()

        for char in s:
            counter[char] = counter.get(char, 0) + 1

        for char in t:
            if char in counter:
                if counter[char] == 1:
                    counter.pop(char)
                else:
                    counter[char] = counter.get(char) - 1

        return len(counter) == 0