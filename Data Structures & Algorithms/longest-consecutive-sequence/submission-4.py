class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        longest = 0

        for n in nums:
            # check if it's the start of a sequence
            if n - 1 not in nums_set:
                length = 0

                # calculate the length of consecutive sequence 
                while n in nums_set:
                    length += 1
                    n += 1
                
                # update the longest length
                longest = max(longest, length)

        return longest