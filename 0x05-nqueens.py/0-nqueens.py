#!/usr/bin/python3
import sys
from typing import List

class Solution:
    def solveNQueens(self, n: int) -> List[List[int]]:
        """Using sets to track columns and diagonals"""
        col = set()
        posDiad = set()
        negDiag = set()
        res = []
        
        """This will store the column positions of the queens for each row"""
        board = [-1] * n  # board[i] will be the column of the queen placed in row i
        
        """Backtracking helper function"""
        def backtrack(r):
            if r == n:  # All queens placed
                """Convert board to a list of [row, column] positions"""
                solution = [[i, board[i]] for i in range(n)]
                res.append(solution)
                return
            for c in range(n):
                """Check if placing a queen at (r, c) is safe"""
                if c in col or (r + c) in posDiad or (r - c) in negDiag:
                    continue
                """Place the queen"""
                board[r] = c
                col.add(c)
                posDiad.add(r + c)
                negDiag.add(r - c)
                
                """Recur to place the next queen"""
                backtrack(r + 1)
                
                """Backtrack (remove the queen)"""
                col.remove(c)
                posDiad.remove(r + c)
                negDiag.remove(r - c)
                board[r] = -1

        """Start backtracking from row 0"""
        backtrack(0)
        return res

def main():
    """Check for the correct number of command line arguments"""
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    
    try:
        """Try to convert the argument to an integer"""
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)
    
    if n < 4:
        print("N must be at least 4")
        sys.exit(1)
    
    """Solve the N-Queens problem"""
    solution = Solution()
    result = solution.solveNQueens(n)
    
    """Print all the solutions"""
    for sol in result:
        print(sol)

if __name__ == "__main__":
    main()
