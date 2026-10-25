class Solution:
    def isPalindrome(self, s: str) -> bool:
        sentence = "".join([c.lower() for c in s if c.isalnum()])

        l, r = 0, len(sentence) - 1

        while l < r:
            if sentence[l] != sentence[r]:
                return False
            
            l += 1
            r -= 1
        
        return True