
def solve():
    n = int(input())
    mat = []
    for _ in range(n):
        mat.append(list(map(int, input().split())))
        
    def iterate(num, r, c):
        check = set()
        for i in range(n):
            if mat[r][i] == num:
                continue
            check.add(mat[r][i])
        
        for i in range(n):
            if abs(mat[i][c] - num) in check:
                return True
        return False
    
    for i in range(n):
        for j in range(n):
            if mat[i][j] == 1:
                continue
            if not iterate(mat[i][j], i, j):
                print("No")
                return
    print("Yes")
            
            

solve()