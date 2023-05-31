n = int(input())
arr = map(int, input().split())

array = list(arr)
array.sort(reverse=True)
for i in array:
    if i < array[0]:
        print(i)
        break
    