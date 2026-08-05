class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        res = 0
        count = 1
        sett = set(nums)
        sett2 = set()
        l = 0
        if len(nums) == 1:
            res = 1
        else:
            while l < len(nums):
                count = 1
                if nums[l] not in sett2:
                    while nums[l] + count in sett:
                        count += 1
                        sett2.add(nums[l] + count)
                res = max(res, count)
                l += 1
        return res