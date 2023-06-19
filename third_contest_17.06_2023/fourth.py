n = int(input())

#if number is positivem no advantage is gained from removing anything
if n >= 0:
    print(n)
else:
    n = str(n)
    #get value obtained from removing last integer
    rem_last = int(n[:-1])
    #get value obtained from removing last but one
    rem_last_but_1 = int(n[:-2]+n[-1])
    #get the larger of the two
    n = max(rem_last, rem_last_but_1)

    print(n)