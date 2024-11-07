
text =input("Entera a String:")


char_count = {}

for char in text:
    char_count[char] = char_count.get(char, 0) + 1


most_frequent_char = max(char_count, key=char_count.get)
frequency = char_count[most_frequent_char]

print(f"The most frequent character is: '{most_frequent_char}' with {frequency} occurrences.")
