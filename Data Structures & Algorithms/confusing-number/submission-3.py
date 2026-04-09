class Solution:
    def confusingNumber(self, n: int) -> bool:
        confusing_nums = {"0":"0", "1":"1", "8":"8", "6":"9", "9":"6"}
        reversed_num = []

        for digit in str(n):
            if digit not in confusing_nums:
                return False
            
            reversed_num.append(confusing_nums[digit])
        
        reversed_num = "".join(reversed_num)

        return int(reversed_num[::-1]) != n