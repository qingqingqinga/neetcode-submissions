class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])
        left, right = 0, m * n - 1

        while left <= right:
            mid = left + (right - left) // 2
            mid_row = mid % n
            mid_col = mid // n
            val = matrix[mid_col][mid_row]

            if  val > target:
                right = mid -1
            elif val == target:
                return True
            else:
                left = mid + 1
        return False
        