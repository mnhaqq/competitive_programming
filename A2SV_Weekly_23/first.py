def solve():
    s = input()

    if len(s) % 2 != 0:
        print("NO")
        return
    
    diff = len(s)//2
    for i in range(diff, len(s)):
        if s[i] != s[i-diff]:
            print("NO")
            return
    print("YES")

t = int(input())
for _ in range(t):
    solve()