class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights) - 1
        max_so_far = 0

        while l < r:
            distance = r - l
            area = min(heights[l], heights[r]) * distance
            max_so_far = max(max_so_far, area)

            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1

        return max_so_far