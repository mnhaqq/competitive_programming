setA = input().split()
setA = set(setA)
num_subsets = int(input())
for _ in range(num_subsets):
    setB = set(input().split())
    if not (setA.issuperset(setB) and len(setA) != len(setB)):
        print(False)
        exit()
print(True)