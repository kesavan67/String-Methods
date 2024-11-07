
text = input("Enter a value of string:")

words = text.split()

longest_word = max(words, key=len)


text = longest_word

print(f"The string with the longest word is: {text}")
