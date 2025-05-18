#You are given an m x n binary matrix grid, where 0 represents a sea cell and 1 represents a land cell.
#
#A move consists of walking from one land cell to another adjacent (4-directionally) land cell or walking off the boundary of the grid.
#
#Return the number of land cells in grid for which we cannot walk off the boundary of the grid in any number of moves.
#
 
#Input: grid =  [[0,0,0,0],
#                [1,0,1,0],
#                [0,1,1,0],
#                [0,0,0,0]
#                ]
#
#Output: 3
#Explanation: There are three 1s that are enclosed by 0s, and one 1 that is not enclosed because its on the boundary.

#Input: grid = [
#                [0,1,1,0]
#                [0,0,1,0]
#                [0,0,1,0]
#                [0,0,0,0]
#                ]
#Output: 0
#Explanation: All 1s are either on the boundary or can reach the boundary.

from typing import List

class Solution:
    def num_enclaves(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]:
            return 0
            
        m, n = len(grid), len(grid[0])
        visited = set()  # Using a set with tuple coordinates for clarity
        
        # DFS to mark all land cells connected to the boundary
        def dfs_mark_boundary_connected(i, j):
            if (i < 0 or i >= m or j < 0 or j >= n or 
                grid[i][j] == 0 or (i, j) in visited):
                return
                
            visited.add((i, j))
            # Check all 4 directions
            dfs_mark_boundary_connected(i+1, j)
            dfs_mark_boundary_connected(i-1, j)
            dfs_mark_boundary_connected(i, j+1)
            dfs_mark_boundary_connected(i, j-1)
        
        # Mark all land cells on the boundary and their connected cells
        for i in range(m):
            if grid[i][0] == 1:  # Left boundary
                dfs_mark_boundary_connected(i, 0)
            if grid[i][n-1] == 1:  # Right boundary
                dfs_mark_boundary_connected(i, n-1)
                
        for j in range(n):
            if grid[0][j] == 1:  # Top boundary
                dfs_mark_boundary_connected(0, j)
            if grid[m-1][j] == 1:  # Bottom boundary
                dfs_mark_boundary_connected(m-1, j)
        
        # Count land cells that are not connected to the boundary
        count = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1 and (i, j) not in visited:
                    count += 1
                    
        return count

def main():
    grid = [
        [0,0,0,0],
        [0,1,1,0],
        [0,0,1,0],
        [0,0,0,0]]
    solution = Solution()
    print(solution.num_enclaves(grid))


main()
