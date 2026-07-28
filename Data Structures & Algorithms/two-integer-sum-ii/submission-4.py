class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        res = []
        numbers.sort()

        print(numbers)

        for i in range(len(numbers)):
            if len(res) == 2:
                break
            r = len(numbers) - 1
            while r > i:
                if numbers[i] + numbers[r] != target:
                    r -= 1
                else:
                    res += [i + 1, r + 1]
                    break
        return res