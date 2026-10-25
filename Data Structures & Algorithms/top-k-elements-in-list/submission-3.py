class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = {}
        bucket = [[] for n in range(len(nums) + 1)]

        for n in nums:
            if n not in d:
                d[n] = 0
            d[n] += 1
        
        for key, value in d.items():
            bucket[value].append(key)
        
        result = []
        
        for i in range(len(bucket) - 1, 0, -1):
            for num in bucket[i]:
                result.append(num)
                if len(result) == k:
                    return result
