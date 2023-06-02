class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:

        l = 0
        r = len(nums) - 1
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] < target:
                l = mid + 1
            elif nums[mid] > target:
                r = mid - 1
            else:
                return mid
        return l

    
# Algorithm with O(log n) runtime complexity

# 1] Initialize left = 0, which will store the required index
# 2] right = len(nums) - 1, num = size of the array
# 3] use while left <= right
# 4] For middle index mid = left+ right / 2
# 5] In if case num[mid] < target, then left = mid + 1 and move to the right half using left = mid + 1
# 6] In Else if block leaves, then num[mid] > target, we move to the left half using right = mid – 1 
# 7] Else Return mid
# 8] after while, return left 
