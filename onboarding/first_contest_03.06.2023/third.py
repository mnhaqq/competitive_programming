n = int(input())
points = input().split()
points = [int(point) for point in points]

num_amazing = 0
mini = points[0]
maxi = points[0]
for point in points:
    if point > maxi:
        maxi = point
        num_amazing+=1
    elif point < mini:
        mini = point
        num_amazing+=1 

print(num_amazing)