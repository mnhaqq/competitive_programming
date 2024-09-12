from collections import Counter

money_earned = 0
num_shoes = int(input())
shoe_sizes = input().split()
num_customers = int(input())

shoe_sizes = [int(shoe) for shoe in shoe_sizes]
shoe_sizes = Counter(shoe_sizes)

for customer in range(num_customers):
    customer_request = input().split()
    if shoe_sizes[int(customer_request[0])] > 0:
        shoe_sizes[int(customer_request[0])]-=1
        money_earned+=int(customer_request[1])

print(money_earned)