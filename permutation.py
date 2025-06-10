class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        curr = []
        n = len(nums)
        added = set()

        def dfs(curr, xlen):
            if xlen ==  n:
                res.append(curr[:])
                return
            
            for num in nums:
                if not num in added:
                    added.add(num)
                    curr.append(num)
                    dfs(curr, xlen + 1)
                    added.remove(num)
                    curr.pop()

        dfs([], 0)
        return res

