t = int(input())

for _ in range(t):
    empty = input()
    chessboard = []
    for row in range(8):
        chessboard.append(input())
    
    
    i = 0
    while i < 8:
        j = 0
        check = []
        while j < 8:
            if chessboard[i][j] == "#":
                check.append(j)
                idx = j
            j+=1
        while len(check) < 2:
            check.append(0)
        if check[1] - check[0] == 2:
            print(i+2, idx)
            break
        i+=1
