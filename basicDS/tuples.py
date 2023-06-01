if __name__ == '__main__':
    n = int(input())
    integer_list = tuple(map(int, input().split()))
    print(type(integer_list))
    print(hash(integer_list))