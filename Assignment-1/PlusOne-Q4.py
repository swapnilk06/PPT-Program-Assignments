from typing import List

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        
        n = len(digits)
    # move along the input array starting from the end
        for i in range(n):
            indx = n - 1 - i
    # set all the 9 at the end of array to 0
            if digits[indx] == 9:
                digits[indx] = 0
    # here we have the rightmost not 9
            else:
    # increase this rightmost not 9 by 1
                digits[indx] += 1
                return digits
    # we're here because all the digits are 9   
        return [1] + digits

input_list = [1,2,3]
obj = Solution()
print(obj.plusOne(input_list))