def solve():
    n, m, k = map(int, input().split())
    a = input()
    b = input()
    
    a = sorted(a)
    b = sorted(b)
    
    c = ""
    
    p1 = p2 = 0
    consec_a = consec_b = 0
    while p1 < n and p2 < m:
        if consec_a == k:
            c += b[p2]
            consec_b += 1
            consec_a = 0
            p2 += 1
        elif consec_b == k:
            c += a[p1]
            consec_a += 1
            consec_b = 0
            p1 += 1
        elif a[p1] <= b[p2] and consec_a < k:
            c += a[p1]
            consec_a += 1
            consec_b = 0
            p1 += 1
        elif b[p2] < a[p1] and consec_b < k:
            c += b[p2]
            consec_b += 1
            consec_a = 0
            p2 += 1
        
    
    print(c)

t = int(input())
for _ in range(t):
    solve()