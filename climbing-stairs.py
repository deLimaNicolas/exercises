class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [0, 1]
        i = 0

        while i < n:
            tmp = dp[1]
            dp[1] = sum(dp)
            dp[0] = tmp
            i += 1
        
        return dp[1]
