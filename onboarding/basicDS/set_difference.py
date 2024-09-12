num_english = int(input())
english_roll_numbers = input().split()
num_french = int(input())
french_roll_numbers = input().split()

english_roll_numbers = set([int(i) for i in english_roll_numbers])
french_roll_numbers = set([int(i) for i in french_roll_numbers])

print(len(english_roll_numbers.difference(french_roll_numbers)))