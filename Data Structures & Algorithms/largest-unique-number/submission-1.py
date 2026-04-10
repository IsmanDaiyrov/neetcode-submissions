class Solution:
    def largestUniqueNumber(self, nums: List[int]) -> int:
        counts = Counter(nums)
        max_so_far = -1

        for v, k in counts.items():
            if k == 1:
                max_so_far = max(max_so_far, v)

        return max_so_far