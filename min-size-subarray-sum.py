class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        minLen = float("inf")

        curSum = 0
        l = r = 0

        for r in range(len(nums)):
            curSum += nums[r]
            while curSum >= target:
                minLen = min(minLen, r - l + 1)
                curSum -= nums[l]
                l += 1

        return minLen if minLen != float("inf") else 0
