n = int(input())
members = input().split()
bad = input().split()

for member in members:
    if member in bad:
        members.remove(member)
count = 0
for member in members:
    arr = " ".join(member)
    arr = arr.split()
    testset = set(arr)
    if len(testset) != len(arr):
        count+=1

print(len(members)-count)