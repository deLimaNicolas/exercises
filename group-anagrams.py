#Given an array of strings strs, group the anagrams together. You can return the answer in any order.
#
# 
#
#Example 1:
#
#Input: strs = ["eat","tea","tan","ate","nat","bat"]
#
#Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
#
#Explanation:
#
#There is no string in strs that can be rearranged to form "bat".
#The strings "nat" and "tan" are anagrams as they can be rearranged to form each other.
#The strings "ate", "eat", and "tea" are anagrams as they can be rearranged to form each other.
#Example 2:
#
#Input: strs = [""]
#
#Output: [[""]]
#
#Example 3:
#
#Input: strs = ["a"]
#
#Output: [["a"]]
#
from typing import List
from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:    
        ans = defaultdict(list)

        for s in strs:
            count = [0] * 26

            for c in s:
                count[ord(c) - ord("a")] += 1
            ans[tuple(count)].append(s)
        print(ans) 
        return list(ans.values())
