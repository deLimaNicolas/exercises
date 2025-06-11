class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        mRows = set()
        mCols = set()
        mPosDia = set()
        mNegDia = set()
        board = [["." for _ in range(n) ] for _ in range(n)]

        res = []

        def backtrack(r):
            if r >= n:
                formatted = ["".join(row) for row in board]
                res.append(formatted)
                return
            
            for c in range(n):
                if (
                    not c in mCols and
                    not r in mRows and
                    not (c + r) in mPosDia and
                    not (r - c) in mNegDia
                ):
                    board[r][c] = "Q"
                    mCols.add(c)
                    mRows.add(r)
                    mPosDia.add(c+r)
                    mNegDia.add(r-c)
                    backtrack(r + 1)

                    board[r][c] = "."
                    mCols.remove(c)
                    mRows.remove(r)
                    mPosDia.remove(c+r)
                    mNegDia.remove(r-c)

        backtrack(0)
        return res



        
