class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if grid[0][0] == 0:
            queue = deque([(0, 0)])
            length = 0
            visited = set()

            ROWS, COLS = len(grid), len(grid[0])

            while len(queue):
                for i in range(len(queue)):
                    r, c = queue.popleft()
                    if (
                        not (r, c) in visited and
                        r >= 0 and c >= 0 and r < ROWS and c < COLS and
                        grid[r][c] == 0
                    ):
                        visited.add((r, c))
                        queue.append((r + 1, c))
                        queue.append((r - 1, c))
                        queue.append((r, c + 1))
                        queue.append((r, c - 1))

                        queue.append((r - 1, c + 1))
                        queue.append((r - 1, c - 1))
                        queue.append((r + 1, c - 1))
                        queue.append((r + 1, c + 1))
                        if r == ROWS - 1 and c == COLS - 1:
                            return length + 1

                length += 1

        return -1
