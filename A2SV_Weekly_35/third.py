from math import gcd

def solve():
    n = int(input())
    a = list(map(int, input().split()))

    gcd_ = a[0]
    for i in range(1, n):
        gcd_ = gcd(gcd_, a[i])

    if gcd_ not in a:
        print(-1)
    else:
        print(gcd_)

solve()