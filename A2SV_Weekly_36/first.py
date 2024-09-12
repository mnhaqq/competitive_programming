from math import factorial

def solve():
    m = int(input())
    a = list(map(int, input().split()))
    
    uniq = len(set(a))
    print(factorial(uniq))
    
        

solve()