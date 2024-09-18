from collections import Counter

def solve():
    n = int(input())
    arr = list(map(int, input().split()))
    
    dic =  Counter(arr)
    ans = float('inf')
    for a, b in dic.items():
        if b == 1:
            ans = min(ans, a)
    if ans == float('inf'):
        print(-1)
    else:
        print(arr.index(ans) + 1)

t = int(input())
for _ in range(t):
    solve()