import math

n = int(input())

elements = list(map(int, input().split()))

less_than_zero = set()
greater_than_zero = set()
equal_to_zero = set()

for i in elements:
    if i > 0:
        greater_than_zero.add(i)
        break
if len(greater_than_zero) == 0:
    count = 0
    for i in elements:
        if i < 0:
            if count == 2:
                break
            greater_than_zero.add(i)
            count+=1
elements = [i for i in elements if i not in greater_than_zero]

for i in elements:
    if i < 0:
        less_than_zero.add(i)
        break
elements = [i for i in elements if i not in less_than_zero]

for i in elements:
    equal_to_zero.add(i)

print(len(less_than_zero), *less_than_zero)
print(len(greater_than_zero), *greater_than_zero)
print(len(equal_to_zero), *equal_to_zero)