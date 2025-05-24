#
#
#
# Input: board = [
#        ["A","B","C","E"],
#        ["S","F","C","S"],
#        ["A","D","E","E"]],
# board = [[]] = false
# string = "" = False
#        word = "ABCCED"
# word maxLength = 15
# wordLength = word.len
#
#   def existWord(postion, letterIdx):
#       if position outside board return 
#       if position in visitedCells return 
#       if letterIdx > wordLength return TRUE
#      if board[postion] == word[letterIdx]:
#           existWord([positions], letterIdx + 1)
#         
#   
#   for x in board.len:
#       for y in board[i].len:
#           visitedCells = set()
#           if existWord([x, y], letterIdx)
#                return True
#    return False
# Output: true
#
#
from typing import List
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
       if not board:
            return False
       if not board[0]:
            return False

       WORD_LEN = len(word)
       ROWS = len(board)
       COLS = len(board[0])

       def existing(position, letterIdx):
           row, col = position
           if letterIdx >= WORD_LEN:
               return True

           if (
               row < 0 or
               row >= ROWS or
               col < 0 or
               col >= COLS
           ):
               return False

           print("Checking ", board[row][col])

           if (row, col) in visitedCells or board[row][col] != word[letterIdx]:
               return False
           visitedCells.add((row, col))

           found = (
           existing([row + 1, col], letterIdx + 1) or
           existing([row - 1, col], letterIdx + 1) or
           existing([row, col + 1], letterIdx + 1) or
           existing([row, col - 1], letterIdx + 1) 
           )

           visitedCells.remove((row, col))
           return found




       for row in range(ROWS):
           for col in range(COLS):
               visitedCells = set()
               print("NEWWWWW ----- ")
               a = existing([row, col], 0)
               if a:
                   return True
       return False

def main():
    solution = Solution()
    result = solution.exist([
        ["A","B","C","E"],
        ["S","F","C","S"],
        ["A","D","E","E"]], "SEE")
    print(result)



main()
