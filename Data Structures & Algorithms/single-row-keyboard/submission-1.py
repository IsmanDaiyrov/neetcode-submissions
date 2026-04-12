class Solution:
    def calculateTime(self, keyboard: str, word: str) -> int:
        res = 0
        keyboard_map = {}
        curr_idx = 0

        for i, char in enumerate(keyboard):
            keyboard_map[char] = i

        for char in word:
            dist = abs(curr_idx - keyboard_map[char])
            res += dist
            curr_idx = keyboard_map[char]

        return res