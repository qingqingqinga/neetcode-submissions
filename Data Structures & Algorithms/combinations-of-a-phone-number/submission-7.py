class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        
        res = []
        digitToChar = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }

        def backtrack(index,path):
            if index == len(digits):
                res.append(path.copy())
                return
            
            for c in range(digitToChar[digits[index]]):
                backtrack(index + 1,path + c)
                path.pop()
        if digits:
            backtrack(0,[])

        return res






        def backtrack(index,path):
            if len(path) >= len(digits):
                res.append(''.join(path)) #把字符串加起来 这个是一个新的字符串
                return
            
            for c in digitToChar[digits[index]]:
                path.append(c)
                backtrack(index + 1,path)
                path.pop() #就算pop也只是pop 一个字符
        if digits:
            backtrack(0,[])
        
        return res











        def backtrack(i,path):
            if len(path) == len(digits):
                res.append(path) #字符串是不可变的 可以直接
                return
            
            for c in digitToChar[digits[i]]:
                backtrack(i + 1,path + c)
        if digits:   
            backtrack(0,"")
        return res