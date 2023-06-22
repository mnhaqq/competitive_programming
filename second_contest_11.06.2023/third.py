def solve():
    n = int(input())
    a = list(map(int, input().split()))
    tmp = []
    for i in range(len(a)):
        tmp.append([a[i], i])
    a = tmp
    a.sort()

    print(n-1)
    for i in range(1, n):
        x = a[i-1][0] - (a[i][0] % a[i-1][0])
        a[i][0] += x
        print(a[i][1]+1, x)
  
t = int(input())
for _ in range(t):
    solve()