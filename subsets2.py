class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = set()
        nums.sort()

        def dfs(i, curr):
            res.add(tuple(curr[:]))
            if i >= len(nums):
                return
            
            curr.append(nums[i])
            dfs(i + 1, curr)
            curr.pop()
            while i < len(nums) - 1 and nums[i] == nums[i + 1]:
                i +=1
            dfs(i + 1, curr)

        dfs(0, [])
        return [list(elm) for elm in res]
