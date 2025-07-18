class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix = {0: 1}
        curr = 0
        res = 0

        for num in nums:
            curr += num
            res += prefix.get((curr - k), 0)
            prefix[curr] = prefix.get(curr, 0) + 1

        return res
