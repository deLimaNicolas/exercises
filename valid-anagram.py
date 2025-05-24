#Given two strings s and t, return true if t is an anagram of s, and false otherwise.
#
# 
#
#Example 1:
#
#Input: s = "anagram", t = "nagaram"
#
#Output: true
#
#Example 2:
#
#Input: s = "rat", t = "car"
#
#Output: false
#
# 
#
#Constraints:
#
#1 <= s.length, t.length <= 5 * 104
#s and t consist of lowercase English letters.




class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # O(n) solution using character frequency counting
        if len(s) != len(t):
            return False
        
        # Single pass character frequency tracking
        char_count = {}
        for char in s:
            char_count[char] = char_count.get(char, 0) + 1
        
        # Subtract frequencies, ensuring zero at end
        for char in t:
            if char not in char_count:
                return False
            char_count[char] -= 1
            if char_count[char] < 0:
                return False
        
        return all(count == 0 for count in char_count.values())


