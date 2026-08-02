class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_dict = {}
        for index, val in enumerate(nums):
            goal = target - val

            if goal in nums_dict:
                return [nums_dict[goal], index]
            else:
                nums_dict[val] = index
        return []