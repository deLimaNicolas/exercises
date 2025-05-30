#Permutation in String
#You are given two strings s1 and s2.
#
#Return true if s2 contains a permutation of s1, or false otherwise. That means if a permutation of s1 exists as a substring of s2, then return true.
#
#Both strings only contain lowercase letters.
#
#Example 1:
#
# {
#    a: 1,
#    b: 1,
#    c: 1
# }


#   loop each letter until pointer reaches belonging to set
#       counter = 0
#       reduce 1 in set
#       while new pointer to the right belong to set
#           reduce 1 in set
#           if counter == s1Len:
#                return True
#           r + 1
#       reset set
#       
#Input: s1 = "abc", s2 = "lecacbe"
#                            |
#                             |
#
#Output: true
#Explanation: The substring "cab" is a permutation of "abc" and is present in "lecabee".
#
#Example 2:
#
#Input: s1 = "abc", s2 = "lecaabee"
#                            |
#                            |
#
#Output: false
#Constraints:
#
#1 <= s1.length, s2.length <= 1000
from collections import Counter

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1Len = len(s1)
        s2Len = len(s2)
        countSet = Counter(s1)
        auxCounter = countSet.copy()

        if not s1 or not s2:
            return False
        if s1Len > s2Len:
            return False

        for ltr in set(s1):
            for idx in range(s2Len):
                if s2[idx] == ltr:
                    auxCounter[s2[idx]] -= 1
                    counter = 1
                    if counter >= s1Len:
                        return True
                    r = idx + 1
                    while (
                        r < s2Len and
                        s2[r] in auxCounter and
                        auxCounter[s2[r]] > 0
                    ):
                        auxCounter[s2[r]] -= 1
                        counter += 1
                        r += 1
                        if counter >= s1Len:
                            return True
                    auxCounter = countSet.copy()

        return False


def main():
    solution = Solution()
    print(solution.checkInclusion("h", "h"))


main()
