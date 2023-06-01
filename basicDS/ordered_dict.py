from collections import OrderedDict

num_items = int(input())
items_dict = OrderedDict()
items = []

for _ in range(num_items):
    item = input().split()
    price = int(item.pop())
    item_name = " ".join(item)
    items_dict[item_name] = price + items_dict.get(item_name, 0)

for key,value in items_dict.items():
    print(key, value)