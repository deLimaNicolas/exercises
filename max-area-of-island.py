class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        maxArea = 0
        visited = set()
        ROWS, COLS = len(grid), len(grid[0])

        def dfs(r, c):
            if(
                r < 0 or r >= ROWS or
                c < 0 or c >= COLS or
                grid[r][c] == 0 or
                (r, c) in visited
            ):
                return 
            
            visited.add((r, c))
            self.cArea += 1

            dfs(r + 1, c),
            dfs(r - 1, c),
            dfs(r, c + 1),
            dfs(r, c - 1),
        
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1 and not (r, c) in visited:
                    self.cArea = 0
                    dfs(r, c)
                    maxArea = max(self.cArea, maxArea)
        return maxArea
