def solve():
    n, m, k = map(int, input().split())
    
    num = (k-1)//2
    l = num // m + 1
    d = num % m + 1
    
    if k % 2 == 0:
        print(l, d, 'R')
    else:
        print(l, d, 'L')
solve()