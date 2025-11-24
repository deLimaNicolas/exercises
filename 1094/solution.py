class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        trips_m = [] # start, to, num_passengers

        for num, start, to in trips:
            trips_m.append((start, to, num))
        
        trips_m.sort(reverse=True)

        pq = [] # free_point, num_pass
        while trips_m:
            start, to, num_pass = trips_m.pop()

            while pq and pq[0][0] <= start:
                _, free_spots = heapq.heappop(pq)
                capacity += free_spots

            capacity -= num_pass
            if capacity < 0:
                return False
            heapq.heappush(pq, (to, num_pass))

        return True
