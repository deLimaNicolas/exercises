class Solution:
    def isPalindrome(self, s: str) -> bool:
        if not s:
            return False
        filteredS = ""

        for ltr in s:
            if ltr.isalnum():
                filteredS += ltr.lower()
        right = len(filteredS) - 1
        left = 0

        while right >=left:
            leftChar = filteredS[left]
            rightChar = filteredS[right]

            if leftChar != rightChar:
                return False

            left += 1
            right -= 1
        return True

       

def main():
    s = "A man, a plan, a canal: Panama"
    solution = Solution()
    solution.isPalindrome(s)

main()

