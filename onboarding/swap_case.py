def swap_case(s):
    new_string = ''
    for letter in s:
        if letter.isupper():
            new_string += letter.lower()
        else:
            new_string += letter.upper()
    return new_string

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)