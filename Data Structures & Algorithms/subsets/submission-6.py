class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        subset = []

        def backtrack(i):
            if i >= len(nums):
                res.append(subset.copy())
                return
            
            
            subset.append(nums[i])
            backtrack(i + 1)

            subset.pop()
            backtrack(i + 1)
        backtrack(0)
        return res

        def backtrack(i,path):
            if i == len(nums):
                res.append(path)
                return 
            
            backtrack(i + 1,path +  [nums[i]])

            backtrack(i + 1,path)
        
        backtrack(0,[])
        return res

        res = []
        subset = []

        def backtrack(index):
            if len(nums) == len(subset):
                res.append(subset.copy())
                return
            
            subset.append(nums[index])
            backtrack(index + 1)

            subset.pop()
            backtrack(index + 1)
        
        backtrack(0)
        return res
        