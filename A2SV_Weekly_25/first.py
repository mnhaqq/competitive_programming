def solve():
    n = int(input())
    a = list(map(int, input().split()))

    a = [(a[i], i) for i in range(n)]
    a.sort()

    for i in range(n//2):
        print(a[i][1]+1, a[n-i-1][1]+1)

solve()