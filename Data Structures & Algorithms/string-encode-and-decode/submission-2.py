class Solution:

    def encode(self, strs: List[str]) -> str:
        master = ""
        for s in strs:
            master += f"{len(s)}#{s}"
            # 5#Hello5#World
        return master

    def decode(self, s: str) -> List[str]:
        master = []
        r = 0
        l = 0

        while r < len(s):
            if s[r] == '#':
                val = int(s[l:r])

                master.append(s[r + 1: r + 1 + val])
                
                r = r + val + 1
                l = r
            else:
                r += 1
        
        return master