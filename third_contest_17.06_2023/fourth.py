n = int(input())

if n >= 0:
    print(n)
else:
    n = str(n)
    rem_last = int(n[:-1])
    rem_last_but_1 = int(n[:-2]+n[-1])
    n = max(rem_last, rem_last_but_1)

    print(n)