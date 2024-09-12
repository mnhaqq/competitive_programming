n = int(input())
friends = list(map(int, input().split()))

#sort friends in increasing order into a temporary array: sorted_friends
sorted_friends = sorted(friends)
final = []

#the problem was basically asking the one based index of the numbers in the input
#so I used the sorted array and appended the indexes to final
for friend in sorted_friends:
    final.append(friends.index(friend)+1)

print(*final)