import math

n = int(input())

arr = list(map(int, input().split()))

i = 0
while i < len(arr):
    if arr[i] < 0:
        i+=1
        continue
    if math.sqrt(arr[i]) % 1 == 0:
        arr.remove(arr[i])
    else:
        i+=1

print(max(arr))