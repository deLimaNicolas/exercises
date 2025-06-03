from typing import List
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        tp = temperatures
        res = [0 for _ in range(len(tp))] 
        stack = [(tp[0], 0)]

        for idx in range(len(tp)):
            while stack and tp[idx] > stack[-1][0]:
                lastValue, lastIndex = stack.pop()
                res[lastIndex] = idx - lastIndex
            stack.append((tp[idx], idx))
        return res
