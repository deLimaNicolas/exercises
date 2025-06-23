class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        LEN = len(nums)
        ans = [0] * LEN * 2    
        for i in range(LEN):
            ans[i] = nums[i]
            ans[i + LEN] = nums[i]

        return ans
