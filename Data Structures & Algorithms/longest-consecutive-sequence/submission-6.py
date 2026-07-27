class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums.sort()

        l = 0
        result = 0
        great = 1

        if len(nums) <= 1:
            loop_r = 0
        else:
            loop_r = 1

        for r in range(loop_r, len(nums)):
            if nums[r] - nums[l] == 1:
                great  += 1
                l += 1
            elif nums[r] == nums[l]:
                l += 1
            else:
                l = r
                great = 1
            
            result = max(great, result)
            
        return result