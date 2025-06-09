class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # Use nlargest with key function - cleaner and more efficient
        return heapq.nsmallest(k, points, key=lambda point: point[0]**2 + point[1]**2)
