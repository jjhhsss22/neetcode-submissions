class Solution:

    def encode(self, strs: List[str]) -> str:
        
        cipher = ""

        for string in strs:
            n = len(string)

            delimiter = "#" + str(n) + "#"

            cipher += delimiter + string

        return cipher

    def decode(self, s: str) -> List[str]:
        if s == "":
            return []

        n = 0
        plain = []

        while n < len(s):
            if s[n] == "#":

                i = n + 1

                while i < len(s):
                    if s[i] == "#":
                        next_idx = i
                        break
                    
                    i += 1
                
                count = int(s[n + 1 : next_idx])
                n = next_idx + 1

                plain.append(s[n : n + count])
                n += count

        return plain
