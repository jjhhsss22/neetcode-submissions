class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        hash_set = set()
        left = 0
        right = 0
        max_length = 0

        while right < len(s):
            current = s[right]
            if current not in hash_set:
                right += 1
                hash_set.add(current)
            else:
                hash_set.remove(s[left])
                left += 1

            current_lenght = right - left
            max_length = max(max_length, current_lenght)

        return max_length