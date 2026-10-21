class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        brackets = {
            ")" : "(",
            "]" : "[",
            "}" : "{"
        }

        for c in s:
            print(stack)
            if c not in brackets:
                stack.append(c)
                continue
            
            if len(stack) != 0 and stack[-1] == brackets[c]:
                stack.pop()
            else:
                return False
        
        return len(stack) == 0