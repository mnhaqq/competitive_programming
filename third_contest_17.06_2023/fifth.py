def solve():
    len_arr = int(input())
    arr = list(map(int, input().split()))

    if max(arr) - min(arr) >= len_arr:
        print("YES")
        print(*[1, len_arr]) 
        return

    for i in range(len_arr-1):
        if max(arr[i:i+2]) - min(arr[i:i+2]) >= 2:
            print("YES")
            print(*[i+1, i+2])
            return
    print("NO")

t = int(input())
for _ in range(t):
    solve()