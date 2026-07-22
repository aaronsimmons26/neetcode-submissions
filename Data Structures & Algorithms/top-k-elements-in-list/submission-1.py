class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        nums_dict = {}

        for num in nums:
            if num in nums_dict:
                nums_dict[num] += 1
            else:
                nums_dict[num] = 1

        largest = sorted(nums_dict.items(), key=lambda number: number[1], reverse=True)[:k]

        answer = [number[0] for number in largest]
        
        return answer

