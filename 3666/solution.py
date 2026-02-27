class Solution:
    def minOperations(self, s: str, k: int) -> int:
        n = len(s)
        z = s.count('0')  # number of zeros to eliminate

        # Edge case: operation size equals string length
        # Flipping everything at once
        if n == k:
            if z == 0:   return 0   # already all 1s
            elif z == n: return 1   # all 0s, one flip fixes it
            else:        return -1  # mixed, can't fix with full flip

        ans = inf

        # Case 1: use even number of operations
        # Each op covers k positions going forward, or (n-k) going backward
        # We need enough ops to cover all zeros either way
        if z % 2 == 0:
            m = max(ceil(z / k), ceil(z / (n - k)))
            if m % 2 == 1:  # force even
                m += 1
            ans = min(ans, m)

        # Case 2: use odd number of operations
        # Now we also need to cover the (n-z) ones without breaking them
        if z % 2 == k % 2:
            m = max(ceil(z / k), ceil((n - z) / (n - k)))
            if m % 2 == 0:  # force odd
                m += 1
            ans = min(ans, m)

        return ans if ans < inf else -1
