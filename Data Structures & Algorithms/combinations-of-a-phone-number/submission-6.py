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
            if len(path) >= len(digits):
                res.append(''.join(path))
                return
            
            for c in digitToChar[digits[index]]:
                path.append(c)
                backtrack(index + 1,path)
                path.pop()
        if digits:
            backtrack(0,[])
        
        return res











        def backtrack(i,path):
            if len(path) == len(digits):
                res.append(path)
                return
            
            for c in digitToChar[digits[i]]:
                backtrack(i + 1,path + c)
        if digits:   
            backtrack(0,"")
        return res