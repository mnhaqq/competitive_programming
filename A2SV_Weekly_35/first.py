def solve():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()

    if n == 1:
        print(a[0])
    for i in range(1, n-1):
        if a[i] - a[i-1] == a[i+1] - a[i]:
            print(a[i])
    print(a[n//2])
    

solve()