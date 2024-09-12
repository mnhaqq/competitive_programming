from collections import Counter

def solve():
    n = int(input())
    a = list(map(int, input().split()))
    
    dic = Counter(a)
    maxx = -1
    for a, b in dic.items():
        if b > maxx:
            maxx = b
    print(n - maxx)

t = int(input())
for _ in range(t):
    solve()