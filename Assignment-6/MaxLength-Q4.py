class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        max_len = 0
        count = 0
        length = len(nums)
        # Create an array of length 2n + 1
        arr = [None] * (2 * length + 1)
        arr[length] = -1
        for i in range(len(nums)):
            if nums[i] == 0:
                count -= 1
            else:
                count += 1
                
            if arr[count + length] is None:
                arr[count + length] = i
            else:
                max_len = max(max_len, i - arr[count + length])
        return max_len
