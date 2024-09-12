def solve():
    n, h = map(int, input().split())
    a = list(map(int, input().split()))

    def check(num):
        ans = num
        for i in range(n-1):
            ans += min(num, a[i+1] - a[i])
        return ans

    l, r = 1, 10 ** 18
    while l <= r:
        mid = (l + r) // 2        
        if check(mid) < h:
            l = mid + 1
        else:
            r = mid - 1
    print(r+1)


t = int(input())    
for _ in range(t):
    solve()