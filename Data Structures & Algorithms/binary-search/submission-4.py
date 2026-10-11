class Solution:
    def search(self, nums: List[int], target: int) -> int:
        return self.binary_search(0, len(nums) - 1, nums, target)
        
    def binary_search(self, lower, upper, nums, target):

        if lower > upper:
            return -1

        midpoint = (upper + lower) // 2

        if nums[midpoint] == target:
            return midpoint
        elif nums[midpoint] < target:
            return self.binary_search(midpoint + 1, upper, nums, target)
        else:
            return self.binary_search(lower, midpoint - 1, nums, target)