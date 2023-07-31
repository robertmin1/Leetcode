class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # Create a 2D array to store the number of unique paths for each cell
        dp = [[0] * n for _ in range(m)]

        # There is one unique path to reach any cell in the first row or first column (moving only right or down)
        for i in range(m):
            dp[i][0] = 1
        for j in range(n):
            dp[0][j] = 1

        # Calculate the number of unique paths for each cell in the grid
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i-1][j] + dp[i][j-1]

        return dp[m-1][n-1]
