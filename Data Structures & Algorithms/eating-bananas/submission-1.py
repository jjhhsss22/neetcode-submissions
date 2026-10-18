class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        left = 1
        right = max(piles)
        ans = max(piles)

        while left <= right:
            mid = (left + right) // 2

            if self.findHours(mid, piles) <= h:
                ans = mid
                right = mid - 1
            else:
                left = mid + 1

        return ans


    def findHours(self, speed, piles):
        time = 0

        for bananas in piles:
            time += math.ceil(bananas / speed)

        return time