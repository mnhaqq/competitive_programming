def solve():
    n, m = map(int, input().split())

    if m > n:
        print("NO")
        return

    if (n - m) % 2 == 0:
        print("YES")
    else:
        print("NO")

t = int(input())
for _ in range(t):
    solve()