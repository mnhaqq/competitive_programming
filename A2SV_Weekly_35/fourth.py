def solve():
    q = int(input())

    ans = []
    for i in range(q):
        n = int(input())
        moves = 0
        while n > 1:
            if n % 5 == 0:
                n = (4 * n) // 5
            elif n % 3 == 0:
                n = (2 * n) // 3
            elif n % 2 == 0:
                n = n // 2
            else:
                moves = -1
                break
            moves += 1
        ans.append(moves)
    for i in ans:
        print(i)

solve()