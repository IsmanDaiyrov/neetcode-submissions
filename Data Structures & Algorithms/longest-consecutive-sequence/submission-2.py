class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seen = set(nums)
        longest_so_far = 1
        curr_longest = 1

        if not nums:
            return 0

        for n in nums:
            while n + 1 in seen:
                curr_longest += 1
                n += 1
            
            longest_so_far = max(longest_so_far, curr_longest)
            curr_longest = 1

        return longest_so_far