def solve():
    n = int(input())
    h = list(map(int, input().split()))
    
    dp = [-1] * n
    dp[-1] = h[-1]
    
    for i in range(n-2, -1, -1):
        dp[i] = max(h[i], dp[i+1] + 1)
    print(max(dp))

t = int(input())
for _ in range(t):
    solve()