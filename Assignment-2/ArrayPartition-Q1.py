class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:

        nums.sort()
    
        a = 0
        for i in range(len(nums)//2):
            a+=nums[2*i]
        return a
