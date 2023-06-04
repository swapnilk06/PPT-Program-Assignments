class Solution:
    def findTheDistanceValue(self, a: List[int], b: List[int], d: int) -> int:
        b.sort()
        res, n = len(a), len(b)
        for val in a:
            left, right = 0, n - 1
            while left <= right:
                mid = (left + right) >> 1
                if abs(b[mid] - val) <= d:
                    res -= 1
                    break
                elif b[mid] > val:
                    right = mid - 1
                else:
                    left = mid + 1
        return res
