class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        maxStones = [elm * (- 1) for elm in stones]
        heapq.heapify(maxStones)

        while len(maxStones) > 1:
            val = -(heapq.heappop(maxStones)) - (-(heapq.heappop(maxStones)))
            if val > 0:
                heapq.heappush(maxStones, (val * -1))
        

        if len(maxStones):
            return maxStones[0] * -1

        return 0
