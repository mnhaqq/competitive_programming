class Solution:
    def countPrimes(self, n: int) -> int:
        if n <= 2:
            return 0        
        is_prime = [True] * n
        is_prime[0] = is_prime[1] = False
        i = 2
        while i < n:
            if is_prime[i] and i**2 <= n:
                j = i**2
                while j < n:
                    is_prime[j] = False
                    j+=i
            i+=1
        prime_count = is_prime.count(True)
        return prime_count

