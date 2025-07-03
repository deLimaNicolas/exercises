class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        LEN1, LEN2 = len(text1), len(text2)
        cache = {}

        def dfs(row, col):
            if row >= LEN1 or col >= LEN2:
                return 0
            if (row, col) in cache:
                return cache[(row, col)]
            
            if text1[row] == text2[col]:
                cache[(row, col)] = 1 + dfs(row + 1, col + 1)
            else:
                cache[(row, col)] = max(
                    dfs(row + 1, col),
                    dfs(row, col + 1)
                )

            return cache[(row, col)]

        return dfs(0, 0)
