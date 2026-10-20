class Solution:
    def rob(self, nums: List[int]) -> int:
        cache = dict()
        return self.dfs(nums, 0, cache)

    def dfs(self, nums, i, cache):
        if i > len(nums) - 1:
            return 0

        if i in cache:
            return cache[i]
        else:
            max_value = max(self.dfs(nums, i + 1, cache), nums[i] + self.dfs(nums, i + 2, cache))
            cache[i] = max_value
    

        return max_value
    
