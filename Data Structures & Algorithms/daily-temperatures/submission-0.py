class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        length = len(temperatures)
        ans = [0] * length

        for i in range(length):
            
            while stack and temperatures[i] > temperatures[stack[-1]]:
                pre_idx = stack.pop()
                ans[pre_idx] = i - pre_idx
            stack.append(i) 
        return ans

        