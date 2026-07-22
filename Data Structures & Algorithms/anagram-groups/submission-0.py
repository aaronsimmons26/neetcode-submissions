class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = {}
        sorted_strs = ["".join(sorted(word)) for word in strs]

        for i in range(len(sorted_strs)):
            if sorted_strs[i] in anagrams:
                anagrams[sorted_strs[i]].append(strs[i])
            else:
                anagrams[sorted_strs[i]] = [strs[i]]

        return[value for (key, value) in anagrams.items()]