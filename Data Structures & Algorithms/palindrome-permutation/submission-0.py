class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        counts = Counter(s)

        if len(s) % 2 == 0:
            for char in counts.values():
                if char % 2 != 0:
                    return False

            return True

        odd_counter = 0

        if len(s) % 2 != 0:
            for char in counts.values():
                if char % 2 != 0:
                    odd_counter += 1

            return True if odd_counter == 1 else False