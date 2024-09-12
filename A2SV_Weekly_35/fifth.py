def solve():
    word, match = input().split()

    check = set()
    p1 = p2 = 0
    while p1 < len(match) and p2 < len(word):
        if word[p2] == match[p1]:
            check.add(word[p2])
            p1 += 1
        p2 += 1

    if p1 < len(match):
        print("NO")
        return

    for i in range(p2, len(word)):
        if word[i] in check:
            print("NO")
            return
    print("YES")

t = int(input())
for _ in range(t):
    solve()