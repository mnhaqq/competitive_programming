from collections import OrderedDict

array = []
dic = OrderedDict()
num_lines = int(input())
for _ in range(num_lines):
    array.append(input())
    word = array.pop()
    dic[word] = dic.get(word, 0) + 1

print(len(dic))
for value in dic.values():
    print(value, end=" ")