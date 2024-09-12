test_cases = int(input())
for test in range(test_cases):
    n = int(input())
    array = [i for i in range(1, n+1)]
    current_sum = sum(array)
    next_greater = (current_sum//n + 1) * n
    difference = next_greater - current_sum
    array[0]+=difference
    print(*array)