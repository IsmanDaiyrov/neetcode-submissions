class Solution:
    def confusingNumber(self, n: int) -> bool:
        confusing_nums = set([0, 1, 6, 8, 9])
        new_num = ""

        for digit in str(n):
            if int(digit) not in confusing_nums:
                return False
            
            if int(digit) == 6:
                new_num += "9"
            elif int(digit) == 9:
                new_num += "6"
            else:
                new_num += digit

        return int(new_num[::-1]) != n