# Remove all occurrences of val in nums in-place

from typing import List

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        
        count = 0          
        for i in range(len(nums)):         
            if nums[i] != val:
                nums[count] = nums[i]
                count += 1
        return count


if __name__ == '__main__':
    r = Solution()
    print(r.removeElement([2, 3, 3, 2], 3))