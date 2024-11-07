
text = input("Enter a String:")


char_count = {}

for char in text:
    char_count[char] = char_count.get(char, 0) + 1


unique_chars = [char for char, count in char_count.items() if count == 1]


print(f"Unique characters: {unique_chars}")
