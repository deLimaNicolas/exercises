class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        ROW = len(matrix)
        COL = len(matrix[0])
        self.sumMat = [[0] * (COL + 1) for _ in range(ROW + 1)]

        for row in range(ROW):
            prefix = 0
            for col in range(COL):
                prefix += matrix[row][col]
                above = self.sumMat[row][col + 1]
                self.sumMat[row + 1][col + 1] = prefix + above
        
    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        row1, col1, row2, col2 = row1 + 1, col1 + 1, row2 + 1, col2 + 1
        bottomRight = self.sumMat[row2][col2]
        minusLeft = self.sumMat[row2][col1 - 1]
        minusTop = self.sumMat[row1 - 1][col2]
        topLeft = self.sumMat[row1 - 1][col1 - 1]
        return bottomRight + topLeft - minusTop - minusLeft
        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)
