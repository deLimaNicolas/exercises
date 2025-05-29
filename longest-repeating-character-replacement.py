#Longest Repeating Character Replacement
#You are given a string s consisting of only uppercase english characters and an integer k. You can choose up to k characters of the string and replace them with any other uppercase English character.
#
#After performing at most k replacements, return the length of the longest substring which contains only one distinct character.
#
#Example 1:
#
#Input: s = "XYYX", k = 2
#
#Output: 4
#Explanation: Either replace the 'X's with 'Y's, or replace the 'Y's with 'X's.
#
#Example 2:
#
# distinctCount = 1
# availableSwitch = 1
# longest = 6
#Input: s = "AAABBAZAAAAAABB", k = 1
#
#Output: 5
#Constraints:
#
#1 <= s.length <= 1000
#0 <= k <= s.length

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        res = 0
        charSet = set(s)

        for c in charSet:
            count = l = 0
            for r in range(len(s)):
                if s[r] == c:
                    count += 1

                while (r - l + 1) - count > k:
                    if s[l] == c:
                        count -= 1
                    l += 1

                res = max(res, r - l + 1)
        return res

def main():
    solution = Solution()
    print(solution.characterReplacement("ABABBA", 2))


main()

