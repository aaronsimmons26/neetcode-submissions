class Solution:

    def encode(self, strs: List[str]) -> str:
        string = ""
        for s in strs:
            string += "".join(f"{len(s)}#" + s)
        return string

    def decode(self, s: str) -> List[str]:
        val, i = [], 0

        while i != len(s):
            j = i
            while s[j] != '#':
                j += 1
            length = int(s[i:j])
            val.append(s[j + 1: j + length + 1])
            i = j + length + 1
        return val