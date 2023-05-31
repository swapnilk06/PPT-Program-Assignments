from typing import List

class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:


        result = [0, 0]
        numsLen = len(nums)
        nums = sorted(nums)
        num = 0
        for i in range(numsLen - 1):
            num ^= (i + 1)
            if nums[i] == nums[i + 1]:
                result[0] = nums[i]
            else:
                num ^= nums[i]
        result[1] = num ^ numsLen ^ nums[numsLen - 1]
        return result

input_list = [1,2,3]
obj = Solution()
print(obj.findErrorNums(input_list))