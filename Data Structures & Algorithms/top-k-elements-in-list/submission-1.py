class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count ={}


        for n in nums:
            count[n] = count.get(n,0) + 1

        freq = []

        for _ in range(len(nums)+1):
            freq.append([])


        for n , c in count.items():
            freq[c].append(n)


        res = []

        for shelf in reversed(freq):
            for n in shelf:
                res.append(n)

                if len(res)== k :
                    return res
        