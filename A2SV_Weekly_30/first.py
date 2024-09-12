def solve():
    n, k = map(int, input().split())
    s =input()

    dic = dict()
    for i in range(k):
        dic[chr(ord("A")+i)] = 0
    
    for i in range(n):
        dic[s[i]] += 1
    
    ans = min(dic.values()) * k
    print(ans)

solve()