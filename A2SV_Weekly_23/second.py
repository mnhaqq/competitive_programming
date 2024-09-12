from collections import defaultdict

def solve():
    n = int(input())
    p = list(map(int, input().split()))

    adj_list = defaultdict(list)
    for i in range(n):
        adj_list[i+1].append(p[i])
    
    visited = set()
    def dfs(node):
        if node in visited:
            return
        
        visited.add(node)
        for nei in adj_list[node]:
            if nei not in visited:
                dfs(nei)

    ans = 0
    for i in range(n):
        if p[i] not in visited:
            dfs(p[i])
            ans += 1
    print(ans)

solve()