class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = {} #num:freq
        res = []

        for num in nums:
            hashmap[num] = 1 + hashmap.get(num,0)
           
        
        freq = [[] for i in range(len(nums) + 1)]

        for n, c in hashmap.items():
            freq[c].append(n)  # freq:num

        for i in range(len(freq) - 1, 0, -1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res
        



       