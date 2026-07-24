import math

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        products, i = [], 0

        while i < len(nums):
            x = nums[i]
            del nums[i]
            product = math.prod(nums)
            products.append(product)
            nums.insert(i, x)
            i += 1
        return products