class Solution:
    def isPalindrome(self, s: str) -> bool:
        phrase = "".join([l for l in s if l.isalnum()]).lower()

        r = len(phrase) - 1
        palindrome = True

        for l in range(len(phrase)):
            if phrase[l] == phrase[r]:
                palindrome = True
                r -= 1
            else:
                palindrome = False
                break

        return palindrome

