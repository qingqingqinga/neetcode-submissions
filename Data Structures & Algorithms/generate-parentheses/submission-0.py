class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []
        self.backtracking(n, result, 0, 0, "")
        return result

    def backtracking(self, n: int, result: List[str], left: int, right: int, s: str) -> None:
        # 右括号多于左括号，非法，剪枝
        if right > left:
            return
        # 左右括号都用完了，得到一个有效组合
        if left == n and right == n:
            result.append(s)
            return
        # 还可以加左括号
        if left < n:
            self.backtracking(n, result, left + 1, right, s + "(")
        # 还可以加右括号（必须满足右括号数量小于左括号）
        if right < left:
            self.backtracking(n, result, left, right + 1, s + ")")
        