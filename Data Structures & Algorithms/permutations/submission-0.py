class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []

        def dfs(arr, used):
            if len(arr) == len(nums):
                res.append(arr.copy())
                return

            for j in range(len(nums)):
                if not used[j]:
                    used[j] = True
                    arr.append(nums[j])
                    dfs(arr, used)
                    arr.pop()
                    used[j] = False

        dfs([], [False] * len(nums))
        return res