class Solution:
    def maxArea(self, heights: List[int]) -> int:
        right = len(heights) - 1
        left = 0
        max_area = 0

        while left < right:
            left_bar = heights[left]
            right_bar = heights[right]

            height = min(left_bar, right_bar)
            width = right - left
            current_area = height * width

            max_area = max(max_area, current_area)

            if left_bar > right_bar:
                right -= 1
            else:
                left += 1

        return max_area

