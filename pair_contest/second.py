def solve():
    n = int(input())
    i = j = 0
    order = "ABBA"
    
    s = a = b = 0
    
    for i in range(1, n+1):
        if s == n:
            break
        if s + i > n:
            if order[j] == "A":
                a += n - s
            else:
                b += n - s
            break
        if order[j] == "A":
            a += i
        else:
            b += i
        s += i
        j += 1
        j %= 4
    print(a, b)

t = int(input())
for _ in range(t):
    solve()