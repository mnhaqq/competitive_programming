import re
t = int(input())

for _ in range(t):
    store = dict()
    digits = []
    s = input().split()
    new_array = []
    new_digits = []
    for word in s:
        digits.append(re.findall("[0-9]", word))
        
    for digit in digits:
        digit = "".join(digit)
        digit = int(digit)
        new_digits.append(digit)
    new_digits = [int(i) for i in new_digits]
    
    i = 0
    while i < len(s):
        store[s[i]] = new_digits[i] 
        i+=1
    store = dict(sorted(store.items(), key=lambda x:x[1]))
    
    for key, value in store.items():
        new_array.append(key)

    final_array = []
    for word in new_array:
        final_array.append(re.sub("[0-9]", "", word))
    
    print(*final_array)
