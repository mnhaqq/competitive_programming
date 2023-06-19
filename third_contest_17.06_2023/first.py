n = int(input())

friends = list(map(int, input().split()))
sorted_friends = sorted(friends)
final = []
for friend in sorted_friends:
    final.append(friends.index(friend)+1)

print(*final)