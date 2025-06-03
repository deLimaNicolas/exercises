from typing import List
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        res = [-1, -1]
        
        LEN = len(nums)
        l, r = 0, LEN - 1 
        
        while l <= r:
        
            mid = l + (r - l) // 2
            
            if nums[mid] == target:
                res[0] = mid
                res[1] = mid
                i = 1
                while mid - i >= 0 and nums[mid - i] == target:
                    res[0] = mid - i
                    i += 1
                    
                i = 1
                while mid + i < LEN and nums[mid + i] == target:
                    res[1] = mid + i
                    i += 1
                return res    
                    
           
            if nums[mid] < target:
                l = mid + 1
                
            if nums[mid] > target:
                r = mid - 1
            
        return res

