class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        if not obstacleGrid or obstacleGrid[-1][-1] == 1 or obstacleGrid[0][0] == 1:
            return 0

        ROWS, COLS = len(obstacleGrid), len(obstacleGrid[0])
        # Format bottom row
        bottomRow = [0] * COLS
        bottomRow[-1] = 1

        # Format right most column
        rightCols = [0] * ROWS
        rightCols[-1] = 1

        # If find any obstacle, set return values as 0 instead of 1
        setValue = 1
        for cellPos in range(COLS - 2, -1, -1):
            if obstacleGrid[ROWS - 1][cellPos] == 1:
                setValue = 0
            bottomRow[cellPos] = setValue

        # If find any obstacle, set return values as 0 instead of 1
        setValue = 1
        for cellPos in range(ROWS - 2, -1, -1):
            if obstacleGrid[cellPos][COLS - 1] == 1:
                setValue = 0
            rightCols[cellPos] = setValue

        prevRow = bottomRow

        i = 1
        while i <= ROWS - 1:
            curRow = [0] * COLS
            curRow[-1] = rightCols[ROWS - i - 1]

            for j in range(COLS - 2, -1, -1):
                valueToSet = (curRow[j + 1] + prevRow[j]) if obstacleGrid[ROWS - i - 1][j] == 0 else 0
                curRow[j] = valueToSet
            prevRow = curRow
            i += 1
        
        return prevRow[0]
