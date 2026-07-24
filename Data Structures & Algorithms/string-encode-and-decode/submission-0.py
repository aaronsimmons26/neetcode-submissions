class Solution:

    def encode(self, strs: List[str]) -> str:
        string = ""

        for i in range(len(strs)):
            word_len = len(strs[i])
            string += "".join(f"{word_len}#" + strs[i])

        return string

    def decode(self, s: str) -> List[str]:
        res, i = [], 0

        while i < len(s):
            j = i
            while s[j] != '#':
                j += 1
            length = int(s[i:j])
            res.append(s[j + 1 : j + 1 + length])
            i = j + 1 + length
        
        return res