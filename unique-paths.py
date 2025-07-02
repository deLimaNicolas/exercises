class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        prevRow = [1] * n

        i = 1
        while i < m:
            newRow = [0] * n
            newRow[-1] = 1

            for j in range(n - 2, -1, -1):
                newRow[j] = newRow[j + 1] + prevRow[j]
            print(newRow)
            prevRow = newRow
            i += 1
        
        return prevRow[0]
