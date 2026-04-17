class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l <= r:
            mid = (l + r) // 2

            if nums[mid] == target:
                return mid

            # locate if we are in the left sorted portion
            if nums[mid] >= nums[l]:
                # compare the target value
                if target > nums[mid] or target < nums[l]:
                    l = mid + 1
                else:
                    r = mid - 1
            # locate if we are in the right sorted portion
            else:
                # compare the target value
                if target < nums[mid] or nums[r] < target:
                    r = mid - 1
                else:
                    l = mid + 1

        return -1