n = int(input())

patterns = []
for _ in range(n):
    patterns.append(input())

arranged = []
i = 0
while i < len(patterns[0]):
    idx = []
    for pattern in patterns:
        idx+=pattern[i]
    idx="".join(idx)
    arranged.append(idx)
    i+=1

final = []
for idx in arranged:
    chars = [i for i in idx]
    i = 0
    while i < len(chars):
        if chars[i] == "?":
            chars.remove(chars[i])
        else:
            i+=1
    idx = "".join(chars)

    if len(idx) == 0:
        idx="a"

    if idx.count(idx[0]) == len(idx):
        idx = idx[0]
    else:
        idx = "?"
    final.append(idx)
print("".join(final))

    