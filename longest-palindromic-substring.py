#Given a string s, return the longest palindromic substring in s.
#
# 
#
#Example 1:
#
#Input: s = "babad"
#Output: "bab"
#Explanation: "aba" is also a valid answer.
#Example 2:
#
#Input: s = "cbbd"
#               |r
#               |l
#Output: "bb"
#
#    b a b a a a b d
#    
#    bab
#   cbbbd
#   |r
#   |l
#    
#    
#
#
#Constraints:
#
#1 <= s.length <= 1000
#s consist of only digits and English letters.


class Solution:
    def longestPalindrome(self, s: str):
        string_len = len(s)
        longest_palin = ""
        longest_palin_len = 0

        for letter_position in range(string_len):
            letf_pointer, right_pointer = letter_position, letter_position
            print("Position ", letter_position)
            while(letf_pointer >= 0 and right_pointer < string_len):
                if s[letf_pointer] == s[right_pointer]:
                    if right_pointer - letf_pointer > longest_palin_len:
                        longest_palin_len =  right_pointer - letf_pointer
                        longest_palin = s[letf_pointer:right_pointer + 1]
                        print("New longest palin ", longest_palin)

                letf_pointer -=1
                right_pointer +=1

        for letter_position in range(string_len):
            letf_pointer, right_pointer = letter_position, letter_position + 1
            print("Position ", letter_position)
            while(letf_pointer >= 0 and right_pointer < string_len):
                if s[letf_pointer] == s[right_pointer]:
                    if right_pointer - letf_pointer > longest_palin_len:
                        longest_palin_len =  right_pointer - letf_pointer
                        longest_palin = s[letf_pointer:right_pointer + 1]
                        print("New longest palin ", longest_palin)

                letf_pointer -=1
                right_pointer +=1




def main():
    solution = Solution()
    result = solution.longestPalindrome("baab")
    print(result)

main()

