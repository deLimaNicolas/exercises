class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        def findMax():
            res = 0
            cur = 0
            curMax = float("-inf")

            for num in nums:
                cur = max(cur, 0)
                curMax = max(cur, curMax)
                cur += num 
                res = max(curMax, res)

            return res

        def findMin():
            res = 0
            cur = 0
            curMin = float("inf")

            for num in nums:
                cur = min(cur, 0)
                curMin = min(cur, curMin)
                cur += num 
                res = min(curMin, res)

            return res
        
        total = sum(nums)
        max1 = findMax()
        max2 = total - findMin()

        return max(max1, max2) if max1 > 0 else max(nums)
