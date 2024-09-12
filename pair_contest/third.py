def solve():
    l, r, d = map(int, input().split())
    if d == 1 and l != 1:
        print(1)
        return
    if d < l or d > r:
        print(d)
        return
    
    print(d * (r//d + 1))

t = int(input())
for _ in range(t):
    solve()