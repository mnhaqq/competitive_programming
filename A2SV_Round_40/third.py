def solve():
    n = int(input())
    a = list(map(int, input().split()))
    
    a.sort(reverse=True)
    
    even = []
    odd = []
    for i in range(len(a)):
        if a[i] % 2 == 0:
            even.append(a[i])
        else:
            odd.append(a[i])
    
    alice = bob = 0
    a1 = a2 = b1 = b2 = 0
    turns = 0
    while (a1 < len(even) and b1 < len(even)) or (a2 < len(odd) and b2 < len(odd)):
        if turns % 2 == 0:
            if a1 < len(even) and a2 < len(odd):
                if even[a1] > odd[a2]:
                    alice += even[a1]
                    a1 += 1
                    b1 = a1
                else:
                    a2 += 1
                    b2 = a2
            elif a1 < len(even):
                alice += even[a1]
                a1 += 1
                b1 = a1
            elif a2 < len(odd):
                a2 += 1
                b2 = a2
        
        else:
            if b1 < len(even) and b2 < len(odd):
                if odd[b2] > even[b1]:
                    bob += odd[b2]
                    b2 += 1
                    a2 = b2
                else:
                    b1 += 1
                    a1 = b1
            elif b2 < len(odd):
                bob += odd[b2]
                b2 += 1
                a2 = b2
            elif b1 < len(even):
                b1 += 1
                a1 = b1
        turns += 1
    
    if alice > bob:
        print("Alice")
    elif bob > alice:
        print("Bob")
    else:
        print("Tie")
                
        
    

t = int(input())
for _ in range(t):
    solve()