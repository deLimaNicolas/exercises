class Solution:
    def solveQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        n = len(nums)
        elm_idxs = defaultdict(list)

        def circular_dist(a, b):
            return min(abs(a - b), n - abs(a - b))

        def find_nearest(curr_idxs, q):
            i = bisect_left(curr_idxs, q)
            left = circular_dist(curr_idxs[(i - 1) % len(curr_idxs)], q)
            right = circular_dist(curr_idxs[(i + 1) % len(curr_idxs)], q)
            return min(left, right)

        for idx, num in enumerate(nums):
            elm_idxs[num].append(idx)

        res = []

        for q in queries:
            curr = nums[q]
            curr_idxs = elm_idxs[curr]
            if len(curr_idxs) == 1:
                res.append(-1)
                continue
            else:
                res.append(find_nearest(curr_idxs, q))

        return res
