from collections import Counter

def solve():
    n = int(input())
    a = list(map(int, input().split()))
    
    dic = Counter(a)
    print(max(dic.values()))
    

t = int(input())
for _ in range(t):
    solve()