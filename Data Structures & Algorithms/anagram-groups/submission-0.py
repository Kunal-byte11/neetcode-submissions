class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        from collections import defaultdict

        res = defaultdict(list)

        for s in strs:
            sortedword = "".join(sorted(s))

            res[sortedword].append(s)
        
        return list(res.values())