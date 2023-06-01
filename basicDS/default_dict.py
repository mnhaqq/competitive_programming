_ = input().split()
m = int(_.pop())
n = int(_.pop())

groupA = []
groupB = []
for _ in range(n):
    groupA.append(input())
for _ in range(m):
    groupB.append(input())

for char in groupB:
    if char not in groupA:
        print(-1)
    else:
        print(*[i+1 for (i, value) in enumerate(groupA) if value == char])