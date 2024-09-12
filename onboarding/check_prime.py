def check_prime(n):
    array = list(range(2, n))
    if n < 2:
        return False
    i = 2
    while i <= n/2:
        if n % i == 0:
            return False
        i+=1
    return True

print(check_prime(169))

