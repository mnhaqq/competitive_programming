grid = [[6,2,1,3],[4,2,1,5],[9,2,8,7],[4,1,2,9]]
maximum = 0
for i in range(len(grid[0])-2):
    sum_hourglass = 0
    for j in range(len(grid)-3):
        sum_hourglass = sum(grid[i][j:j+3]) + grid[i+1][j+1] + sum(grid[i+2][j:j+3])
        maximum = max(sum_hourglass, maximum)
print(maximum)