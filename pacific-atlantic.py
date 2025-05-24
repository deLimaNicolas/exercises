from typing import List

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        if not heights:
            return []
        
        pacificRoots = set()
        atlanticRoots = set()

        ROWS, COL = len(heights), len(heights[0])

        def dfs(borderSets, currentPosition, previousPosition):
            if currentPosition[0] < 0 or currentPosition[0] >= ROWS or currentPosition[1] < 0 or currentPosition[1] >= COL:
                return
            previousHeight = heights[previousPosition[0]][previousPosition[1]]
            currentHeight = heights[currentPosition[0]][currentPosition[1]]
            if previousHeight > currentHeight:
                return
            if (currentPosition[0], currentPosition[1]) in borderSets:
                return 
            
            borderSets.add((currentPosition[0], currentPosition[1]))

            dfs(borderSets, [currentPosition[0] + 1, currentPosition[1]], currentPosition)
            dfs(borderSets, [currentPosition[0] - 1, currentPosition[1]], currentPosition)
            dfs(borderSets, [currentPosition[0], currentPosition[1] + 1], currentPosition)
            dfs(borderSets, [currentPosition[0], currentPosition[1] - 1], currentPosition)

        
        # Pacific (left and top edges)
        for row in range(ROWS):
            dfs(pacificRoots, [row, 0], [row, 0])
        for col in range(COL):
            dfs(pacificRoots, [0, col], [0, col])

        # Atlantic (right and bottom edges)
        for row in range(ROWS):
            dfs(atlanticRoots, [row, COL - 1], [row, COL - 1])
        for col in range(COL):
            dfs(atlanticRoots, [ROWS - 1, col], [ROWS - 1, col])


        print(pacificRoots)
        print(atlanticRoots)


        result = []
        for px in range(ROWS):
            for py in range(COL):
                if (px, py) in pacificRoots and (px, py) in atlanticRoots:
                    result.append([px, py])

        return result


#You are given a rectangular island heights where heights[r][c] represents the height above sea level of the cell at coordinate (r, c).

#The islands borders the Pacific Ocean from the top and left sides, and borders the Atlantic Ocean from the bottom and right sides.

#Water can flow in four directions (up, down, left, or right) from a cell to a neighboring cell with height equal or lower. Water can also flow into the ocean from cells adjacent to the ocean.

#Find all cells where water can flow from that cell to both the Pacific and Atlantic oceans. Return it as a 2D list where each element is a list [r, c] representing the row and column of the cell. You may return the answer in any order.



#Input: heights = [
#  [4,2,7,3,4],
#  [7,4,6,4,7],
#  [6,3,5,3,6]
#]

#Output: [[0,2],[0,4],[1,0],[1,1],[1,2],[1,3],[1,4],[2,0]]



class Solution2:
    def pacificAtlantic2(self, heights: List[List[int]]) -> List[List[int]]:
from typing import List

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        if not heights or not heights[0]:
            return []

        ROWS, COLS = len(heights), len(heights[0])
        connectsToPacific = set()
        connectsToAtlantic = set()

        def explorePaths(connectsSet, startX, startY):
            stack = [(startX, startY)]
            connectsSet.add((startX, startY))
            
            while stack:
                currentPX, currentPY = stack.pop()
                
                for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                    newX, newY = currentPX + dx, currentPY + dy
                    
                    if (
                        0 <= newX < ROWS and
                        0 <= newY < COLS and
                        (newX, newY) not in connectsSet and
                        heights[newX][newY] >= heights[currentPX][currentPY]
                    ):
                        connectsSet.add((newX, newY))
                        stack.append((newX, newY))

        # Explore Pacific (left and top edges)
        for row in range(ROWS):
            explorePaths(connectsToPacific, row, 0)
        for col in range(COLS):
            explorePaths(connectsToPacific, 0, col)

        # Explore Atlantic (right and bottom edges)
        for row in range(ROWS):
            explorePaths(connectsToAtlantic, row, COLS - 1)
        for col in range(COLS):
            explorePaths(connectsToAtlantic, ROWS - 1, col)

        # Find intersection
        return [
            [row, col]
            for row in range(ROWS)
            for col in range(COLS)
            if (row, col) in connectsToPacific and (row, col) in connectsToAtlantic
        ]
