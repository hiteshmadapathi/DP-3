# Time Complexity --> O(n*n) where n*n are the dimensions of matrix
# Space Complexity --> O(n*n)
class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        n = len(matrix)
        if n==1:
            return matrix[0][0]

        dp = [[0]*(n) for i in range(n+1)]
        for i in range(1,n+1):
            for j in range(n):
                if j==0:
                    dp[i][j] = matrix[i-1][j] + min(dp[i-1][j], dp[i-1][j+1])
                elif j==n-1:
                    dp[i][j] = matrix[i-1][j] + min(dp[i-1][j-1], dp[i-1][j])
                else:
                    dp[i][j] = matrix[i-1][j] + min(dp[i-1][j-1], dp[i-1][j], dp[i-1][j+1])

        return min(dp[-1][:])



'''
# Time Complexity --> O(n*n) where n*n are the dimensions of matrix
# Space Complexity --> O(n*n)
class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        
        re = float('inf')
        n = len(matrix)
        self.memo = [[float('inf')]*(n) for i in range(n)]
        for i in range(n):
            re = min(re, self.helper(matrix, 0, i))
        return re 


    def helper(self, matrix, row, col):
        # base
        if row==len(matrix):
            return 0
        if self.memo[row][col]!=float('inf'):
            return self.memo[row][col]
        # logic
        if col==0:
            case = matrix[row][col] + min(self.helper(matrix, row+1, col), self.helper(matrix, row+1, col+1))
        elif col==len(matrix)-1:
            case = matrix[row][col] + min(self.helper(matrix, row+1, col-1), self.helper(matrix, row+1, col))
        else:
            case = matrix[row][col]+min(self.helper(matrix, row+1, col-1), self.helper(matrix, row+1, col), self.helper(matrix, row+1, col+1))
        self.memo[row][col] = case
        return case
'''
