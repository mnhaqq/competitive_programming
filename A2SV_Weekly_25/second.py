def solve():
    n, m, k = map(int, input().split())

    total_cost = n * m - 1
    if total_cost == k:
        print('YES')
    else:
        print('NO')

t = int(input())
for _ in range(t):
    solve()