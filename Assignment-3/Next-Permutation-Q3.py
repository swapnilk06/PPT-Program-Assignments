class Solution:
    def nextPermutation(self, nums: List[int]) -> None:

        l=len(nums)-2
        while l>=0:
            if nums[l]<nums[l+1]:
                s=len(nums)-1
                while s>l:
                    if nums[s]>nums[l]:
                        nums[l],nums[s]=nums[s],nums[l] 
                        arr=(nums[:l+1]+sorted(nums[l+1:]))
                        nums[:]=arr[:]
                        return nums
                    s-=1
            l-=1
        else:
            nums.reverse()
            return nums
