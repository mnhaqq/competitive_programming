def solve():
    n = int(input())
    
    ans = n
    for i in range(n // 5 + 1):
        for j in range((n-i * 5) // 3 + 1):
            r = n - (i * 5) - (j * 3)
            ans = min(ans, r)
    print(ans)

t = int(input())
for _ in range(t):
    solve()