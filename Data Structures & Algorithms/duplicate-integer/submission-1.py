class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hash_set = set()

        for number in nums:
            if number in hash_set:
                return True
            else:
                hash_set.add(number)

        return False