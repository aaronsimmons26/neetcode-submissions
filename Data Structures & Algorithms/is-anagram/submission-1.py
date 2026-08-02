class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s = "".join(sorted(l.lower() for l in s))
        t = "".join(sorted(l.lower() for l in t))

        if s == t:
            return True
        else:
            return False
