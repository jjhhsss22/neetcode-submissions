class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "":
            return ""

        tracker = {}

        for c in t:
            tracker[c] = tracker.get(c, 0) + 1

        pointer1 = 0
        pointer2 = 0
        missing = len(t)

        min_length = float("inf")
        min_pointer1, min_pointer2 = 0, 0

        while pointer2 < len(s):
            current_char = s[pointer2]

            if current_char in tracker:
                if tracker[current_char] > 0:
                    missing -= 1
                tracker[current_char] -= 1
                
            while missing == 0:
                if pointer2 - pointer1 + 1 < min_length:
                    min_length = pointer2 - pointer1 + 1
                    min_pointer1 = pointer1
                    min_pointer2 = pointer2 + 1

                if s[pointer1] in tracker:
                    tracker[s[pointer1]] += 1

                    if tracker[s[pointer1]] > 0:
                        missing += 1

                pointer1 += 1

            pointer2 += 1

        return (
            s[min_pointer1:min_pointer2]
            if min_length != float("inf")
            else ""
        )