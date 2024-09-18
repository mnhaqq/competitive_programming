def solve():
    n = int(input())
    a = list(map(int, input().split()))
    
    arr = [(a[i], i) for i in range(n)]
    arr.sort()
    
    def check(i):
        ans = arr[i][0]
        for idx in range(n):
            if idx == i:
                continue
            if ans < arr[idx][0]:
                return False
            ans += arr[idx][0]
        return True
    
    l, h = 0, n-1
    while l < h:
        m = (l+h)//2
        if check(m):
            h = m
        else:
            l = m + 1
    
    ans = []   
    for i in range(h, n):
        ans.append(arr[i][1] + 1)
        
    ans.sort()
    print(len(ans))
    print(*ans)
        
        
        

t = int(input())
for _ in range(t):
    solve()