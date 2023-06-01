class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:

        n = len(nums)
        baseline = 0
        
        for i in range(1, n):
            if nums[i] - nums[i - 1] > 0: 
                baseline = 1
                break
            elif nums[i] - nums[i - 1] < 0:
                baseline = -1
                break
        for i in range(1, n):
            if (nums[i] - nums[i - 1]) * baseline < 0:
                return False
        return True
