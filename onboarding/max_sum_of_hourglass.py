class Solution:
    def maxSum(self, grid: List[List[int]]) -> int:
        maximum = 0
        for i in range(len(grid)-2):
            sum_hourglass = 0
            for j in range(len(grid[0])-2):
                sum_hourglass = sum(grid[i][j:j+3])+grid[i+1][j+1]+sum(grid[i+2][j:j+3])
                maximum = max(sum_hourglass, maximum)
        return maximum