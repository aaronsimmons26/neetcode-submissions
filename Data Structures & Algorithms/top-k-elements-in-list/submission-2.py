class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = {}
        buckets = [[] for num in range(len(nums) + 1)]

        # Step 1: count (yours, already correct)
        for n in nums:
            if n not in d:
                d[n] = 1
            else:
                d[n] += 1

        # Step 2: drop each number into the slot for its count
        for key, value in d.items():
            buckets[value].append(key)          # blank 1 and blank 2

        # Step 3: walk from the biggest count down to 1
        result = []
        for i in range(len(buckets) - 1, 0, -1):
            for num in buckets[i]:
                result.append(num)
                if len(result) == k:                         # blank 3: do we have enough?
                    return result                  # blank 4