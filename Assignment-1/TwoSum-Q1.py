# Two numbers Sum

from typing import List

class Solution(object):
   def twoSum(self, nums, target):
      
      
      required = {}
      for i in range(len(nums)):
            if target - nums[i] in required:
                  return [required[target - nums[i]],i]
            else:
                  required[nums[i]]=i

input_list = [2,7,11,15]
obj = Solution()
print(obj.twoSum(input_list, 9))
