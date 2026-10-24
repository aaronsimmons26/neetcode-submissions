class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        d_s = {}
        d_t = {}

        if len(s) != len(t):
             return False
        for char in s:
            d_s[char] = d_s.get(char, 0) + 1
        for char in t:
            d_t[char] = d_t.get(char, 0) + 1

        return d_s == d_t