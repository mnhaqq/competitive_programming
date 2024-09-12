def solve():
    n, m, x = map(int, input().split())
    length = [m, m]
    ans = 1
    for _ in range(x):
        l, r = map(int, input().split())
        if (l < length[0] and r < length[0]) or (l > length[1] and r > length[1]):
            continue
        if l < length[0]:
            ans += length[0] - l 
            length[0] = l
        if r > length[1]:
            ans += r - length[1]
            length[1] = r
  
    print(ans)
    
    

t = int(input())
for _ in range(t):
    solve()