t = int(input())

for _ in range(t):
    first_rect = list(map(int, input().split()))
    second_rect = list(map(int, input().split()))
    first_rect.sort()
    second_rect.sort()

    if (first_rect[0] == second_rect[0] and first_rect[0] == first_rect[1]+second_rect[1]):
        print("Yes")
    elif (first_rect[1] == second_rect[1] and first_rect[1] == first_rect[0]+second_rect[0]):
        print("Yes")
    else:
        print("No")