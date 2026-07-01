class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]: #计数法和排序法都有
        res = {} # count:s

        for s in strs:
            count = [0] * 26
            for c in s:
                key = ord(c) - ord('a') 
                count[key] += 1
            if tuple(count) not in res:
                res[tuple(count)] = []
                res[tuple(count)].append(s)
            else: 
                res[tuple(count)].append(s)
        return list(res.values())


     