class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        def dfs(i, subset, total):
            if total == target:
                res.append(subset.copy())
                return

            if total > target:
                return

            for j in range(i, len(nums)):
                subset.append(nums[j])
                dfs(j, subset, total + nums[j])
                subset.pop()

        dfs(0, [], 0)
        return res