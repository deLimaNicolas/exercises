class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums or not len(nums):
            return 0
        if len(nums) <= 2:
            return max(nums)
        
        dp = [nums[0], max(nums[1], nums[0])]
        maxRob = max(dp)

        i = 2
        while i < len(nums):
            currRob = max(nums[i] + dp[0], dp[1])
            maxRob = max(currRob, maxRob)
            dp[0] = dp[1]
            dp[1] = currRob
            i += 1
        
        return maxRob
        
