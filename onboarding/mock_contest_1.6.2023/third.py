n = int(input())
new_array = []
for _ in range(n):
    array = input().split("#")
    string = " ".join(array)
    new_array.append(string)

for element in new_array:
    print(element)
    