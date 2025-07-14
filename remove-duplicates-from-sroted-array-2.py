class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        l = r = 0
        
        while r < len(nums):
            nums[l] = nums[r]
            count = 1
            r += 1
            
            while r < len(nums) and nums[l] == nums[r] and count < 2:
                l += 1
                nums[l] = nums[r]
                count += 1
                r += 1
            
            while r < len(nums) and nums[l] == nums[r]:
                r += 1
                
            l += 1
        
        return l
