class Solution:
    def search(self, nums: List[int], target: int) -> int:
         # 1. 找最小值索引（旋转点）
        l1, r1 = 0, len(nums) - 1
        while l1 < r1:
            mid = (l1 + r1) // 2
            if nums[mid] > nums[r1]:
                l1 = mid + 1
            else:
                r1 = mid
        pivot = l1
        def binary_search(left: int,right: int) -> int:
            mid = (left + right) // 2
            while left < right:
                if nums[mid] == target:
                    return mid
                elif nums[mid] > target:
                    right = mid -1
                else:
                    left = mid + 1
            return left


        # 2. 定义二分查找函数（复用）
        def binary_search(left: int, right: int) -> int:
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] == target:
                    return mid
                elif nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
            return -1

        # 3. 确定 target 所在的有序区间
        n = len(nums)
        if target >= nums[0]:
            # 左段 [0, pivot-1]（若 pivot==0 则数组未旋转，左段为整个数组）
            left, right = 0, pivot - 1 if pivot > 0 else n - 1
        else:
            # 右段 [pivot, n-1]
            left, right = pivot, n - 1

        # 4. 在区间内二分查找
        return binary_search(left, right)
        
        l1, r1 = 0 ,len(nums) - 1
        minnum = 0

        # find the pivot : index of the minimum value
        while l1 < r1:
            mid = (l1 + r1) // 2
            if nums[mid] > nums[r1]:
                l1 = mid + 1
            else:
                r1 = mid
        pivot =l1
        minnum = nums[pivot]

        # determine which side the target is on
        l2, r2 = 0, len(nums) - 1

        while l2 < r2:
            if minnum > target: # does not exist
                return -1
            elif minnum == target: 
                return pivot
            else:
                if nums[l2] < nums[r2]:
                    mid = ( r2 + l2 ) // 2
                    if target > nums[mid]:
                        l2 = mid + 1
                    elif target == nums[mid]:
                        return mid
                    else:
                        r2 = mid - 1
                    
                else:
                    if target > nums[r2]:
                        r2 = pivot - 1
                        mid = (r2 + l2) //2
                        if target > nums[mid]:
                            l2 = mid + 1
                        elif target == nums[mid]:
                            return mid
                        else:
                            r2 = mid -1
                    else: 
                        l2 = pivot + 1
                        mid = (r2 + l2) //2
                        if target > nums[mid]:
                            l2 = mid + 1
                        elif target == nums[mid]:
                            return mid
                        else:
                            r2 = mid -1


                return l2





        

    


