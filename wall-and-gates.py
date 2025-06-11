class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        ROWS, COLS = len(rooms), len(rooms[0]) 
        visited = set()

        queue = deque()

        def addRoom(r, c):
            if(
                r < 0 or r >= ROWS or
                c < 0 or c >= COLS or
                (r, c) in visited or
                rooms[r][c] == -1
            ):
                return
            visited.add((r,c))
            queue.append((r,c))

        for r in range(ROWS):
            for c in range(COLS):
                if rooms[r][c] == 0:
                    visited.add((r, c))
                    queue.append((r, c))
        

        dist = 0
        while queue:
            for i in range(len(queue)):
                r, c = queue.popleft()
                rooms[r][c] = dist
                addRoom(r + 1, c)
                addRoom(r - 1, c)
                addRoom(r, c + 1)
                addRoom(r, c - 1)
            dist += 1



            

