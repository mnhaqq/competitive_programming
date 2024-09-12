n = int(input())

phrase = []
for _ in range(n):
    phrase += input().split()

for word in phrase:
    print(word)    
