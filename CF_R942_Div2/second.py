def solve():
    n = int(input())
    s = input()

    if s.count('U') % 2 != 0:
        print("YES")
    else:
        print("NO")

t = int(input())
for _ in range(t):
    solve()