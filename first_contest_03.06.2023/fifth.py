n, k = map(int, input().split())
theorems_taught = list(map(int, input().split()))
behaviors = list(map(int, input().split()))

# calculate number of theorems taught when student was awake already
awake = 0
for index, behavior in enumerate(behaviors):
    if behavior == 1:
        awake+=theorems_taught[index]

# calculate the gain if the secret technique is used at 0 index
gain = 0
for i in range(k):
    if behaviors[i] == 0:
        gain+=theorems_taught[i]

# calculate total theorems if secret technique is used at index 0
max_theorems = awake + gain

# check total theorems if secret technique is used at each place behaviors is 0
# and find max
for i in range(1, n-k+1):
    if behaviors[i+k-1] == 0:
        gain+=theorems_taught[i+k-1]
    if behaviors[i-1] == 0:
        gain-=theorems_taught[i-1]
    max_theorems=max(max_theorems, awake+gain)

print(max_theorems)