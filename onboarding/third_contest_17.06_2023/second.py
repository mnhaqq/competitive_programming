n = int(input())

#taking input for the matrix
matrix = []
for i in range(n):
    matrix.append(list(map(int, input().split())))

#count the rows where two or more people had a value of one
count = 0
for row in matrix:
    if sum(row) >= 2:
        count+=1
print(count)