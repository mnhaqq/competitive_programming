t = int(input())

for _ in range(t):
    len_a = int(input())
    b = list(map(int, input().split()))

    a = [b[0]]
    len_a-=2
    i = 0
    while i < len_a:
        a.append(min(b[i], b[i+1]))
        i+=1

    a.append(b[-1])

    print(*a)
