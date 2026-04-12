class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for word in strs:
            res += str(len(word)) + "#" + word
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0

        while i < len(s):
            # read the number until the # delimeter
            j = i
            while s[j] != "#":
                j += 1
            length = int(s[i:j])

            # append the word:
            # slice it from the delimeter all the way to the end
            res.append(s[j + 1 : j + 1 + length])
            
            # update the index
            i = j + 1 + length

        return res