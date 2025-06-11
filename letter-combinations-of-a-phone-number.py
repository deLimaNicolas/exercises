class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        res = []
        LEN = len(digits)
        digitMap = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }

        def backtrack(i, cur):
            if len(cur) >= LEN:
                res.append("".join(cur[:]))
                return

            for j in range(len(digitMap[digits[i]])):
                cur.append(digitMap[digits[i]][j])
                backtrack(i + 1, cur)
                cur.pop()
                
        backtrack(0, [])
        return res
