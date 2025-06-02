class Solution:
    def isValid(self, s: str) -> bool:
        matchMap = {
            ")": "(",
            "]": "[",
            "}": "{",
        }

        stack = [s[0]]

        for idx in range(1, len(s)):
            currentLtr = s[idx]
            if currentLtr in matchMap:
                if not stack:
                    return False
                cp = stack.pop()
                if matchMap[currentLtr] != cp:
                    return False
            else:
                stack.append(currentLtr)

        if len(stack) != 0:
            return False
        return True
