class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = []

        prefix = []
        suffix = []

        product = 1

        for i in range(len(nums)):
            product *= nums[i]
            prefix.append(product)

        product = 1

        for j in range(len(nums) - 1, -1, -1):
            product *= nums[j]
            suffix.append(product)
        suffix.reverse()

        for k in range(len(nums)):
            if k == 0:
                pre = 1
            else:
                pre = prefix[k - 1]
            if k == len(nums) - 1:
                suf = 1
            else:
                suf = suffix[k + 1]

            result.append(pre * suf)

        return result

        