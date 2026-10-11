class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hash_set = set(nums)
        max_counter = 0

        for number in nums:
            if number - 1 not in hash_set:

                counter = 1
                current = number

                while current + 1 in hash_set:
                    counter += 1
                    current += 1
                
                max_counter = max(max_counter, counter)
            
        return max_counter

