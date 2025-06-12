class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        res = -1

        ROWS, COLS = len(grid), len(grid[0])
        visited = set() 
        self.fresh = 0

        queue = deque()

        def addCell(r, c):
            if(
                r < 0 or r >= ROWS or
                c < 0 or c >= COLS or
                grid[r][c] != 1 or
                (r, c) in visited
            ):
                return
            visited.add((r, c))
            queue.append((r, c))
            self.fresh -= 1

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    self.fresh += 1
                if grid[r][c] == 2:
                    visited.add((r, c))
                    queue.append((r,c))
        if self.fresh == 0:
            return 0
        while queue:
            for i in range(len(queue)):
                r, c = queue.popleft()
                addCell(r - 1, c)
                addCell(r + 1, c)
                addCell(r, c - 1)
                addCell(r, c + 1)
            if queue:
                res += 1

        if res > -1:
            res += 1
        if self.fresh > 0:
            res = -1
        return res
