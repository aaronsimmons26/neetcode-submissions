class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        d_s = {}
        d_t = {}

        if len(s) == len(t):
            for char in s:
                d_s[char] = d_s.get(char, 1) + 1
            
            for char in t:
                d_t[char] = d_t.get(char, 1) + 1
        else:
            return False
            
        if d_s == d_t:
            return True
        else:
            return False