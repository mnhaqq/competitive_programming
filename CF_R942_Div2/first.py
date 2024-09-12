def solve():
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    ans = p1 = p2 = 0
    while p1 < n and p2 < n:
        if a[p1] > b[p2]:
            ans += 1
            p2 += 1
        else:
            p1 += 1
            p2 += 1
    print(ans)

t = int(input())
for _ in range(t):
    solve()