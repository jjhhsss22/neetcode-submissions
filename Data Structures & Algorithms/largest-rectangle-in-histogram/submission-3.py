class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []

        max_area = 0

        for i, h in enumerate(heights):
            min_index = i

            while stack and h < stack[-1][1]:
                top = stack.pop()
                min_index = top[0]
                max_area = max(max_area, top[1] * (i - top[0]))

            stack.append((min_index, h))

        for i, h in stack:
            max_area = max(max_area, h * (len(heights) - i))

        return max_area