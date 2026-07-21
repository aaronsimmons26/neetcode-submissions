class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_sorted = "".join(sorted(s)).lower()
        t_sorted = "".join(sorted(t)).lower()

        if len(s_sorted) == len(t_sorted):
            if s_sorted == t_sorted:
                return True
        return False
