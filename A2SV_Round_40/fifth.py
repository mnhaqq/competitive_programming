def solve():
    n = int(input())
    x = list(map(int, input().split()))
    
    x.sort()
    
    ans = []
    for i in range(n):
        check = set([x[i]])
        for j in range(i):
            if i == j:
                continue
            if bin(abs(x[i] - x[j])).count("1") == 1:
                check.add(x[j])
        ans.append(check)
    
    len_ans = 0
    final = 0
    for i in range(len(ans)):
        if len(ans[i]) == 1 and bin(list(ans[i])[0]).count("1") == 1:
            final = ans[i]
            len_ans = 1
        if len(ans[i]) > len_ans:
            final = ans[i]
            len_ans = len(ans[i])
    
    print(len(final))
    print(*list(final))
            

solve()