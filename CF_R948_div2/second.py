def solve():
    x = int(input())
    
    ans = []
    val = 0
    for i in range(31):
        if x & (1 << i):
            ans.append(1)
            val += (1 << i)
        elif x & (1 << i) and ans:
            ans[-1] = -1
            ans.append(0)
            ans.append(1)
        else:
            ans.append(0)
    
    print(*ans)

t = int(input())
for _ in range(t):
    solve()