n = int(input())

matrix = []
for i in range(n):
    matrix.append(list(map(int, input().split())))

count = 0
for row in matrix:
    if sum(row) >= 2:
        count+=1
print(count)