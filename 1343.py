class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        if k > len(arr):
            return 0
        
        res = 0

        l, r = 0, 0
        cur = 0

        while r < len(arr):
            if (r - l) == k:
                cur -= arr[l]
                l += 1

            cur += arr[r]
            if r + 1 >= k and cur // k >= threshold:
                res += 1
            r += 1

        return res




