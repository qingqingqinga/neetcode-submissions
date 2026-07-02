class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for c in tokens:
            if c == "+":
                stack.append(stack.pop() + stack.pop())
            elif c == "-":
                a,b = stack.pop(),stack.pop()
                stack.append(b - a)
            elif c == "*":
                stack.append(stack.pop() * stack.pop())
            elif c == "/":
                a,b = stack.pop(),stack.pop() #先弹出的是右操作数（a），后弹出的是左操作数（b）
                stack.append(int(float(b) / a)) #truncates toward zero # python2里面不行 
            else:
                stack.append(int(c))
        return stack.pop()
        
        