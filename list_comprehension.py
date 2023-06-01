if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    
    arr1 = [i for i in range(0, x+1)]
    arr2 = [i for i in range(0, y+1)]
    arr3 = [i for i in range(0, z+1)]
    array = [[i,j,k] for i in arr1 for j in arr2 for k in arr3 if i+j+k != n]
    print(array)