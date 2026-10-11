class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product = 1

        ans = []

        for number in nums:
            ans.append(product)

            product *= number

        reversed_num = reversed(nums)

        product = 1

        for i in range(len(nums) - 1, -1, -1):
            ans[i] *= product
            product *= nums[i]
            
        return ans


        