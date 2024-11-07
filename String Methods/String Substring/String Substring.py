
text = "Hello, welcome to the world of Python."


substring = "welcome"


index = text.find(substring)

if index != -1:
    print(f"The substring '{substring}' is found at index {index}.")
else:
    print(f"The substring '{substring}' was not found.")
