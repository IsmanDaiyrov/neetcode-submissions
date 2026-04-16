class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        
        if nums[l] <= nums[r]:
            return nums[l]

        while l < r:
            mid = (l + r) // 2

            # if n > n + 1 => return n + 1
            if nums[mid] > nums[mid + 1]:
                return nums[mid + 1]
            # if mid is greater than the rightmost => we are in the left half
            # min should be in the right half
            elif nums[mid] > nums[r]:
                l = mid + 1
            # otherwise, min is in the left half including mid
            else:
                r = mid
        
        return nums[l]