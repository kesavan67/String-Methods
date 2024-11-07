
text = input("Enter a String")


words = text.split()


longest_word = max(words, key=len)


print(f"The longest word is: {longest_word}")
