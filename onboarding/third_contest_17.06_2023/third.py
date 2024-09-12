import math

n = int(input())
#take input for array
arr = list(map(int, input().split()))

i = 0
while i < len(arr):
    #skip negative numbers
    if arr[i] < 0:
        i+=1
        continue
    #remove perfect squares
    if math.sqrt(arr[i]) % 1 == 0:
        arr.remove(arr[i])
    #skip positive non perfect square
    else:
        i+=1
        
#print the maximum number left
print(max(arr))