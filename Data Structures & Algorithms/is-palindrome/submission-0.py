class Solution:
    def isPalindrome(self, s: str) -> bool:
        data = "".join([char.lower() for char in s if char.isalnum()])

        palindrome = 0

        for i in range(len(data)):
            point1 = data[i]
            point2 = data[-i - 1]

            if point1 == point2:
                palindrome += 1

        if palindrome == len(data):
            return True
        else:
            return False

