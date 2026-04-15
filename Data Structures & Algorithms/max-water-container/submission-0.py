class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_so_far = 0
        l = 0
        r = len(heights) - 1

        while l < r:
            distance = r - l
            max_so_far = max(max_so_far, min(heights[l], heights[r]) * distance)

            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1

        return max_so_far