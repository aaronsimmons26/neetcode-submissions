class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s = "".join(sorted(s)).lower()
        t = "".join(sorted(t)).lower()

        if s == t:
            return True
        else:
            return False
