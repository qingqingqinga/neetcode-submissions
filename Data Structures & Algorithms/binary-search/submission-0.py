class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1  # 区间为 [left, right]，左右都闭合
        
        while left <= right:            # 注意是 <=，因为 left == right 时区间还有一个元素
            mid = left + (right - left) // 2   # 防止 (left+right) 溢出的写法
            
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1          # target 在右半边，排除 mid
            else:
                right = mid - 1         # target 在左半边，排除 mid
        
        return -1                       # 没找到

        