class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        if len(nums) < 2:
            return []

        store = dict()

        for i, number in enumerate(nums):

            if number in store:
                return [store[number], i]
            else:
                store[target - number] = i

        return []