
text = input("Enter a String:")


char_count = {}


for char in text:
    if char in char_count:
        char_count[char] += 1
    else:
        char_count[char] = 1


print(f"Character frequencies: {char_count}")
