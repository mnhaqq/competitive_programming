def solve():
    a = input()
    s = input()
    
    dic = dict()
    for i in range(len(a)):
        dic[a[i]] = i
    
    ans = 0
    for i in range(1, len(s)):
        ans += abs(dic[s[i]] - dic[s[i-1]])

    print(ans)
    
t = int(input())
for _ in range(t):
    solve()